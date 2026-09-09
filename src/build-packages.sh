#!/bin/sh
# Shared build loop used by both test-pr and build CI jobs.
# Required env: PACKAGES, ARCH, BOOTSTRAP, TEST, NATIVE, FORCE
# Writes built=true/false to GITHUB_OUTPUT when that variable is set.
. "${GITHUB_WORKSPACE}/extra/src/pkg-helpers.sh"
export PATH="/opt/xbps/usr/bin/:$PATH"
cd /void-packages

xbps_test=''
[ "$TEST" = 1 ] && xbps_test='-Q'

force_flag=''
[ "$FORCE" = 'true' ] && force_flag='-N'

echo "==> Resolving dependencies for: $PACKAGES"
PKGS=""
_retry=0
while [ -z "$PKGS" ] && [ "$_retry" -lt 3 ]; do
	_retry=$((_retry + 1))
	echo "==> sort-dependencies attempt $_retry/3"
	PKGS=$(sudo -Eu builder ./xbps-src $xbps_test sort-dependencies $PACKAGES 2>/dev/null) || PKGS=""
	[ -z "$PKGS" ] && sleep 5
done
if [ -z "$PKGS" ]; then
	echo "==> ERROR: sort-dependencies failed after 3 attempts"
	exit 1
fi

echo "==> Build order with dependencies:"
echo "$PKGS"
echo

BUILT=false
FAILED=false
for pkg in $PKGS; do
	if ! pkg_arch_ok "$pkg" "$ARCH"; then
		echo "==> Skipping ${pkg}: not available for ${ARCH}"
		continue
	fi

	arch_flag=''
	if [ "$BOOTSTRAP" != "$ARCH" ]; then
		case "$BOOTSTRAP/$ARCH" in
			x86_64/x86_64-musl)
				arch_flag="-A $ARCH"
				;;
			aarch64/aarch64-musl)
				# Build musl target in the aarch64 (glibc) masterdir: run natively
				# on arm64 hardware with musl cross-toolchain (Node is unavailable
				#in a aarch64-musl rootfs, so the musl host image can't host node deps).
				arch_flag="-A aarch64 -a aarch64-musl"
				;;
			*)
				_cnc_visited=""
				if _check_nocross_chain "$pkg"; then
					arch_flag="-A $ARCH"
				else
					arch_flag="-a $ARCH"
				fi
				;;
		esac
	fi

	echo "==> Building ${pkg}"
	if sudo -Eu builder ./xbps-src -j"$(nproc)" -s $force_flag $arch_flag $xbps_test pkg "$pkg"; then
		BUILT=true
	else
		FAILED=true
	fi
	echo
done

[ -n "${GITHUB_OUTPUT:-}" ] && printf 'built=%s\n' "$BUILT" >> "$GITHUB_OUTPUT"
if [ "$FAILED" = true ]; then
	exit 1
fi
exit 0
