#!/usr/bin/env python3
"""Track per-arch CI build results for the README package table.

The status file is `src/build-status.json`, mapping package name to
{
    "version": "...",
    "arches": { "<arch>": {"status": "ok|fail|skip", "run_id": int, "run_date": "YYYY-MM-DD"} }
}

Results are preserved across builds: a package keeps its last recorded
result for each arch until a later run overwrites it.

Subcommands:
    merge RESULTS_DIR STATUS_FILE RUN_ID RUN_DATE
        Merge per-arch result files produced by `build-packages.sh`
        (GitHub artifacts named `build-results-<ARCH>` containing
        `results.tsv` with lines `name<TAB>version<TAB>status`).
        RUN_DATE is the build date (YYYY-MM-DD) stamped on every entry.
        Updates STATUS_FILE in place and prints a per-package summary.

    prune STATUS_FILE PKG...
        Drop entries for PKGs (e.g. templates removed from the repo).

    cell PKG STATUS_FILE
        Print the four arch status cells, the latest CI run id, and the
        run date of that run, one field per line:
            status_x86_64, status_x86_64_musl,
            status_aarch64, status_aarch64_musl, run_id, run_date
        An empty status field means "no data yet".
"""

from __future__ import annotations

import json
import os
import sys

ARCHES = ["x86_64", "x86_64-musl", "aarch64", "aarch64-musl"]
VALID_STATUS = {"ok", "fail", "skip"}


def _load_status(path: str) -> dict:
    if not os.path.isfile(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        sys.stderr.write(f"error: cannot read {path}: {e}\n")
        sys.exit(1)
    if not isinstance(data, dict):
        sys.stderr.write(f"error: {path} is not a JSON object\n")
        sys.exit(1)
    return data


def _save_status(path: str, data: dict) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)


def _run_id_of(arch_entry: dict) -> int:
    try:
        return int(arch_entry.get("run_id") or 0)
    except (TypeError, ValueError):
        return 0


def merge(results_dir: str, status_file: str, run_id: str, run_date: str) -> int:
    data = _load_status(status_file)
    arch_dirs = sorted(
        d for d in os.listdir(results_dir)
        if d.startswith("build-results-") and os.path.isdir(os.path.join(results_dir, d))
    )
    if not arch_dirs:
        print("  no build-result artifacts; nothing to merge")
        return 0

    updated = 0
    for d in arch_dirs:
        arch = d[len("build-results-"):]
        entry = os.path.join(results_dir, d, "results.tsv")
        if not os.path.isfile(entry):
            sys.stderr.write(f"warning: {entry} missing; skipping {arch}\n")
            continue
        with open(entry, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                parts = line.split("\t")
                if len(parts) != 3:
                    sys.stderr.write(f"warning: bad line in {entry}: {line!r}\n")
                    continue
                pkg, version, status = parts
                if status not in VALID_STATUS:
                    sys.stderr.write(f"warning: unknown status {status!r} for {pkg}\n")
                    continue
                rec = data.setdefault(pkg, {"version": version, "arches": {}})
                if not isinstance(rec.get("arches"), dict):
                    rec["arches"] = {}
                rec["version"] = version
                rec["arches"][arch] = {
                    "status": status,
                    "run_id": int(run_id),
                    "run_date": run_date,
                }
                updated += 1
                print(f"  {pkg}: {arch} {status}")

    _save_status(status_file, data)
    print(f"  updated {updated} arch entries in {status_file}")
    return 0


def prune(status_file: str, pkgs: list[str]) -> int:
    data = _load_status(status_file)
    removed = [p for p in pkgs if p in data]
    for p in removed:
        del data[p]
        print(f"  dropped {p}")
    if removed:
        _save_status(status_file, data)
    else:
        print("  nothing to prune")
    return 0


def cell(pkg: str, status_file: str) -> int:
    data = _load_status(status_file)
    rec = data.get(pkg)
    out = [""] * 4
    latest = 0
    latest_date = ""
    if isinstance(rec, dict) and isinstance(rec.get("arches"), dict):
        arches = rec["arches"]
        for i, arch in enumerate(ARCHES):
            entry = arches.get(arch)
            if not isinstance(entry, dict):
                continue
            out[i] = entry.get("status", "")
            rid = _run_id_of(entry)
            if rid > latest:
                latest = rid
                latest_date = entry.get("run_date", "")
    out.append(str(latest) if latest else "")
    out.append(latest_date)
    print("\n".join(out))
    return 0


def main() -> int:
    args = sys.argv[1:]
    if not args:
        sys.stderr.write(f"Usage: {sys.argv[0]} {{merge|prune|cell}} ...\n")
        return 2
    cmd, args = args[0], args[1:]
    if cmd == "merge" and len(args) == 4:
        return merge(*args)
    if cmd == "prune" and len(args) >= 1:
        return prune(args[0], args[1:])
    if cmd == "cell" and len(args) == 2:
        return cell(*args)
    if cmd == "cell" and len(args) < 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} cell PKG STATUS_FILE\n")
        return 2
    sys.stderr.write(f"Usage: {sys.argv[0]} {{merge|prune|cell}} ...\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())