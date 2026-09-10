# PRs welcome 🤗

## This is:
- vOid Community repOsitory (oco)
- aka
- Void User Repository
- VUR
- testing repo
- waiting list
- void unstable

Providing:
- templates
- binaries
- by community
- for community

## DISCLAIMER
This project is **not affiliated with or endorsed by the Void Linux project** or its maintainers.  
It is an **unofficial community repository** designed to simplify managing and building user-contributed packages using the void-packages build system.  
Use at your own discretion.

## Overview
A collection of template files for building packages on Void Linux.  
If you dont wish to build the packages locally,  
https://repo.osowoso.org repository provides prebuilt binaries.  
Pick your architecture there and you will see

## Structure
- Main repository with templates on Codeberg https://codeberg.org/oSoWoSo/oco
- mirror Github repository + CI https://github.com/oSoWoSo/Void_Community_Repository (Here we build binary packages)
- To make CI quicker we use daily updated Bootstrap Docker images from [oco-builder](https://github.com/oSoWoSo/oco-builder)
- nocross templates build support (GitHub aarch runner)
- Binary repository https://repo.osowoso.org/

## What we don't build? (From source)
Browsers: It's waste of energy and when you finish building is maybe already new version out  
We provide repackaged binaries, they all have `-bin` after <pkgname>  
(You can use AppImages and manage them with [AM](https://github.com/ivan-hc/AM), or flatpaks. They are usualy always latest)  

## How to use
in https://repo.osowoso.org/`(architecture)`
are easy to understand READMEs
Just pick your architecture

### Install repository key
```sh
curl -fsSL "https://codeberg.org/oSoWoSo/oco/raw/branch/OCO/keys/oco-repo-key.plist" \
  -o /tmp/oco-repo-key.plist 2>/dev/null || \
curl -fsSL "https://raw.githubusercontent.com/oSoWoSo/Void_Community_Repository/OCO/keys/oco-repo-key.plist" \
  -o /tmp/oco-repo-key.plist
sudo cp /tmp/oco-repo-key.plist /var/db/xbps/keys/oco-repo-key.plist
```

## How to contribute

### Clone using ocoman script
Running `./ocoman -i` will clone void-packages and oco into ~/void  
PS: Destination could be changed look at `./ocoman -h`

### Clone manualy
Clone Codeberg repo  
`git clone https://codeberg.org/oSoWoSo/oco`  
Copy srcpkgs directory to cloned [void-packages](https://github.com/void-linux/void-packages)

Then:

Use `xnew <pkgname>` to create new template  
Fill everyhing as needed and remove rest  
Use `xlint <pkgname>` to lint templates  
Build templates with tests `./xbps-src -Q pkg <pkgname>`  
(Tests must be allowed in $XBPS_DISTDIR/etc/conf)  
We build for x86_64 and aarch64 + musl variants  
(I am usualy trying x86_64 and aarch64-musl crossbuild)  
Add your changes  
When you change any shlib from upstream void-packages, changes must be reflected in `shlibs_remove` and `shlibe_append`  
When you add new shlib add it only to `shlibe_append`  
After adding template, run `./ocoman -u` to regenerate templates list and table  
One commit per template, mesage: `<pkgname> <version>`  

Create PR

## Void official documentation
- [Manual](https://github.com/void-linux/void-packages/blob/master/Manual.md)
- [Contributing](https://github.com/void-linux/void-packages/blob/master/CONTRIBUTING.md)
- [Readme](https://github.com/void-linux/void-packages/blob/master/README.md)

## Available templates (packages when built successfully)
| package | version | home | CI | x86_64 | x86_64-musl | aarch64 | aarch64-musl | maintainer | notes | popis |
|:--------|:--------|:-----|:---|:-------|:------------|:--------|:-------------|:-----------|:------|:------|
| android-sdk | 36 | [home](https://developer.android.com/studio) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31010693888) | ✅ |  |  |  | zenobit | x86_64 | Android SDK platform 36 and build-tools 29.0.3 |
| aquamarine | 0.14.0 | [home](https://github.com/hyprwm/aquamarine) | [2026-08-29](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33280003423) | ❌ | ❌ | ❌ | ❌ | zenobit |  | Aquamarine is a very light linux rendering backend library |
| blocaled | 0.7 | [home](https://github.com/lfs-book/blocaled) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34434384696) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Standalone implementation of the localed D-Bus service |
| brave-browser-bin | 1.94.121 | [home](https://www.brave.com/) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34004323616) | ✅ |  | ✅ |  | zenobit | x86_64 aarch64 | One of the most private browsers built on top off Chromium project |
| brave-origin-bin | 1.94.121 | [home](https://www.brave.com/) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34004836180) | ✅ |  |  |  | zenobit | x86_64 aarc64 | Minimalist browser from the makers of Brave (binary) |
| brow6el | 0.3.5 | [home](https://brow6el.dev/) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31129153059) | ✅ |  |  |  | zenobit | x86_64 | Minimalistic graphical terminal web browser using sixels |
| btrfs-progs | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32567072456) | ❌ | ❌ | ✅ | ✅ | Enno Boland |  | Btrfs filesystem utilities |
| bulletty | 0.3.0 | [home](https://github.com/crocidb/bulletty) | [2026-08-12](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31642775836) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Feed reader for the terminal that stores the articles as Markdown |
| bun | 1.4.0 | [home](https://bun.sh) | [2026-08-28](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33164080978) | ✅ | ❌ | ❌ | ❌ | zenobit | aarch64* x86_64* | JavaScript runtime, bundler, transpiler, and package manager |
| bun-bootstrap | 1.4.0 | [home](https://bun.sh) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32541692981) | ✅ | ✅ | ✅ | ✅ | zenobit | x86_64* aarch64* | Bootstrap package for bun (prebuilt binary) |
| caerus | 0.6.0 | [home](https://github.com/mendescotta/Caerus) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32563631240) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Package manager for Void Linux, inspired by Synaptic |
| candy-icons-git | 0.11.1 | [home](https://www.opendesktop.org/p/1305251/) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31131116243) | ✅ | ✅ | ✅ | ✅ | Trve_AY |  | Sweet gradient icons, sweet rainbow folders included |
| cc-switch | 3.20.1 | [home](https://github.com/farion1231/cc-switch) | [2026-08-29](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33246109775) | ✅ | ✅ | ❌ | ❌ | zenobit | x86_64* aarch64* | Assistant for Claude Code, Codex, OpenCode, OpenClaw & Gemini CLI |
| cliamp | 2.1.0 | [home](https://github.com/bjarneo/cliamp) | [2026-09-07](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34167469661) | ❌ | ❌ | ❌ | ❌ | zenobit |  | Terminal music player inspired by winamp |
| clitest | 0.5.0 | [home](https://github.com/aureliojargas/clitest) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31018256307) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Command Line Tester |
| Community-Repositories-Collection | 1 | [home](https://repo.osowoso.org) | [2026-08-25](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32837630220) | ✅ | ✅ | ✅ | ✅ | zenobit |  | CRC: Collection of community repositories |
| corekeyboard | 5.0.1 | [home](https://gitlab.com/cubocore/coreapps/corekeyboard) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31131156002) | ✅ | ✅ | ✅ | ✅ | zenobit |  | X11 based virtual keyboard for C Suite |
| cosign | 3.1.3 | [home](https://github.com/sigstore/cosign) | [2026-08-14](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31832532827) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Code signing and transparency for containers and binaries |
| cosmic-applets | 1.8.0 | [home](https://github.com/pop-os/cosmic-applets) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428731045) | ✅ | ✅ | – | – | zenobit | x86_64* | Applets for COSMIC Panel |
| cosmic-applibrary | 1.8.0 | [home](https://github.com/pop-os/cosmic-app-library) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428705599) | ✅ | ✅ | – | – | zenobit | x86_64* | Application launcher for the COSMIC desktop |
| cosmic-bg | 1.8.0 | [home](https://github.com/pop-os/cosmic-bg) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428754071) | ✅ | ✅ | – | – | zenobit | x86_64* | COSMIC session service which applies backgrounds to displays |
| cosmic-comp | 1.8.0 | [home](https://github.com/pop-os/cosmic-comp) | [2026-07-02](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28582473145) | ✅ | ✅ | – | – | zenobit | x86_64* | Compositor for the COSMIC desktop environment |
| cosmic-desktop-full | 1.1.0 | [home](https://github.com/pop-os/cosmic-epoch) | [2026-07-01](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28535755721) | ✅ | ✅ | – | – | Bella109 | x86_64* | Full Cosmic Desktop |
| cosmic-desktop-minimal | 1.1.0 | [home](https://github.com/pop-os/cosmic-epoch) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31019465256) | ✅ | ✅ | – | – | Bella109 | x86_64* | Meta Package for COSMIC Desktop |
| cosmic-edit | 1.8.0 | [home](https://github.com/pop-os/cosmic-edit) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428765173) | ✅ | ✅ | – | – | zenobit | x86_64* | Text editor for the COSMIC desktop |
| cosmic-files | 1.8.0 | [home](https://github.com/pop-os/cosmic-files) | [2026-07-02](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28584943014) | ✅ | ✅ | – | – | zenobit | x86_64* | File manager for the COSMIC desktop environment |
| cosmic-greeter | 1.8.0 | [home](https://github.com/pop-os/cosmic-greeter) | [2026-07-02](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28625827149) | ✅ | ✅ | – | – | zenobit | x86_64* | COSMIC greeter for greetd |
| cosmic-icons | 1.8.0 | [home](https://github.com/pop-os/cosmic-icons) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34434408500) | ✅ | ✅ | – | – | zenobit | x86_64* | System76 Cosmic icon theme for Linux |
| cosmic-idle | 1.8.0 | [home](https://github.com/pop-os/cosmic-idle) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428774383) | ✅ | ✅ | – | – | zenobit | x86_64* | Idle daemon for the COSMIC desktop |
| cosmic-initial-setup | 1.8.0 | [home](https://github.com/pop-os/cosmic-initial-setup) | [2026-07-03](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28673960176) | ❌ | ❌ |  |  | zenobit | x86_64* | Initial setup for the COSMIC desktop |
| cosmic-launcher | 1.8.0 | [home](https://github.com/pop-os/cosmic-launcher) | [2026-07-03](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28673973328) | ✅ | ✅ | – | – | zenobit | x86_64* | Layer Shell frontend for pop-launcher |
| cosmic-monitor | 1.8.0 | [home](https://github.com/pop-os/cosmic-monitor) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428784772) | ✅ | ✅ | – | – | zenobit | x86_64* | System monitor for the COSMIC desktop |
| cosmic-notifications | 1.8.0 | [home](https://github.com/pop-os/cosmic-notifications) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428797714) | ✅ | ✅ | – | – | zenobit | x86_64* | Layer Shell notifications daemon for the COSMIC desktop |
| cosmic-osd | 1.8.0 | [home](https://github.com/pop-os/cosmic-osd) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428806612) | ✅ | ✅ | – | – | zenobit | x86_64* | On-Screen Display daemon for the COSMIC desktop |
| cosmic-panel | 1.8.0 | [home](https://github.com/pop-os/cosmic-panel) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428820321) | ✅ | ✅ | – | – | zenobit | x86_64* | COSMIC applet for creating panels and docks |
| cosmic-player | 1.8.0 | [home](https://github.com/pop-os/cosmic-player) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428846661) | ✅ | ✅ | – | – | zenobit | x86_64* | Media player for the COSMIC desktop |
| cosmic-randr | 1.8.0 | [home](https://github.com/pop-os/cosmic-randr) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34434435978) | ✅ | ✅ | – | – | zenobit | x86_64* | Library and utility for displaying and configuring Wayland outputs |
| cosmic-screenshot | 1.8.0 | [home](https://github.com/pop-os/cosmic-screenshot) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428860620) | ✅ | ✅ | – | – | zenobit | x86_64* | Utility for capturing screenshots via XDG Desktop Portal |
| cosmic-session | 1.8.0 | [home](https://github.com/pop-os/cosmic-session) | [2026-07-03](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28684433095) | ✅ | ✅ | – | – | zenobit | x86_64* | Session manager for the COSMIC desktop environment |
| cosmic-settings | 1.8.0 | [home](https://github.com/pop-os/cosmic-settings) | [2026-07-01](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28535755721) |  |  | – | – | zenobit | x86_64* | Settings application for the COSMIC desktop environment |
| cosmic-settings-daemon | 1.8.0 | [home](https://github.com/pop-os/cosmic-settings-daemon) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428877642) | ✅ | ✅ | – | – | zenobit | x86_64* | Settings daemon for the COSMIC desktop environment |
| cosmic-sound-theme | 1.8.0 | [home](https://github.com/pop-os/cosmic-sound-theme) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428897249) | ✅ | ✅ |  |  | zenobit | x86_64* | Sound theme for the COSMIC desktop environment |
| cosmic-store | 1.8.0 | [home](https://github.com/pop-os/cosmic-store) |  |  |  |  |  | zenobit | x86_64* | Cosmic App Store |
| cosmic-term | 1.8.0 | [home](https://github.com/pop-os/cosmic-term) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428913889) | ✅ | ✅ | – | – | zenobit | x86_64* | COSMIC terminal emulator |
| cosmic-tweaks | 0.2.2 | [home](https://github.com/cosmic-utils/cosmic-tweaks) | [2026-07-08](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28964285155) | ✅ |  |  |  | Bella109 | x86_64 | Tweaks for COSMIC |
| cosmic-wallpapers | 1.8.0 | [home](https://github.com/pop-os/cosmic-wallpapers) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428923372) | ✅ | ✅ | – | – | zenobit | x86_64* | Wallpapers for the COSMIC Desktop Environment |
| cosmic-workspaces-epoch | 1.8.0 | [home](https://github.com/pop-os/cosmic-workspaces-epoch) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428960585) | ✅ | ✅ | – | – | zenobit | x86_64* | COSMIC workspaces |
| CRC-black-hole | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-brgvos | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-cereus-core | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-cereus-extra | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-cosmic | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-d77void | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-hyprland | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-jake | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-lazy | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-librewolf | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-noid | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-odyssey | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-sofijacom | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-sonicde | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-split | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-voiders | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-vostock | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| CRC-xlibre | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| crush | 0.90.0 | [home](https://github.com/charmbracelet/crush) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32541893914) | ❌ | ❌ | ❌ | ❌ | zenobit |  | Glamourous AI coding agent for your favourite terminal |
| cwal | 0.10.1 | [home](https://github.com/nitinbhat972/cwal) | [2026-09-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34358432448) | ✅ | ✅ | ✅ | ❌ | zenobit |  | Blazing-fast pywal-like color palette generator written in C |
| dankcalendar | 1.6.1 | [home](https://github.com/AvengeMedia/dankcalendar) | [2026-09-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34372632967) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Calendar app for the Dank Linux desktop (Local, Google, CalDAV, iCloud) |
| DankMaterialShell | 1.5.3 | [home](https://github.com/AvengeMedia/DankMaterialShell) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32571652904) | ✅ | ✅ | ❌ | ❌ | zenobit |  | Desktop shell for wayland compositors built with Quickshell & GO |
| dashy | 4.1.5 | [home](https://github.com/Lissy93/dashy) |  |  |  |  |  | zenobit |  | Self-hostable personal dashboard |
| default-cursors | 1 | [home](https://www.voidlinux.org) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34434426752) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Default cursor set |
| desktop-tui | 0.3.2 | [home](https://github.com/Julien-cpsn/desktop-tui) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31050630933) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Desktop environment without graphics |
| devedeng | 4.22.1 | [home](https://www.rastersoft.com/programas/devede.html) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32548092409) | ✅ | ✅ | ✅ | ❌ | Bella109 |  | Create video DVDs and CDs |
| distrobox | 1.8.2.5 | [home](https://distrobox.it/) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31051133430) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Podman/Docker wrapper to use any linux distribution in your terminal |
| dragonfly-reverb | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31051562621) | ✅ | ✅ | ✅ | ❌ | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-clap | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-doc | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-lv2 | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-standalone | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-vst | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-vst3 | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| drako | 0.3.3 | [home](https://github.com/lucky7xz/drako) | [2026-08-25](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32893940104) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Grid-based, customizable TUI-Deck launcher |
| easybashgui | 15.0.2 | [home](https://github.com/BashGui/easybashgui) |  |  |  |  |  | zenobit |  | Bash functions library that aims to give simple GUI functions |
| faugus-launcher | 2.2.2 | [home](https://github.com/Faugus/faugus-launcher) | [2026-09-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33988032485) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Simple and lightweight app for running Windows games using UMU-Launcher |
| fcitx5-lotus | 3.5.8 | [home](https://github.com/LotusInputMethod/fcitx5-lotus) | [2026-09-04](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33854321813) | ✅ | ✅ | ❌ | ❌ | Coolllyn |  | Vietnamese input method for fcitx5 |
| fcitx5-lotus-settings | 3.5.8 | [home](https://github.com/LotusInputMethod/fcitx5-lotus) |  |  |  |  |  | Coolllyn |  | Vietnamese input method for fcitx5 |
| flyline | 1.7.1 | [home](https://github.com/HalFrgrd/flyline) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34004858784) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Bash plugin to replace readline for a modern line editing experience |
| forgejo-runner | 13.1.0 | [home](https://code.forgejo.org/forgejo/runner) | [2026-09-01](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33485454243) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Continuous integration for Forgejo |
| FreeTube | 0.25.1 | [home](https://github.com/FreeTubeApp/FreeTube) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31052769369) | ✅ |  |  |  | Bella109 | x86_64 | Client for watching YouTube Videos |
| ftxui | 7.0.3 | [home](https://github.com/ArthurSonzogni/FTXUI) | [2026-08-07](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31133776832) | ✅ | ✅ | ✅ | ✅ | zenobit |  | C++ Functional Terminal User Interface |
| ftxui-devel | 7.0.3 | [home](https://github.com/ArthurSonzogni/FTXUI) |  |  |  |  |  | zenobit |  | C++ Functional Terminal User Interface |
| gama | 1.2.1 | [home](https://github.com/termkit/gama) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31053471992) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Manage your GitHub Actions from Terminal with great UI |
| gh-dash | 4.25.2 | [home](https://github.com/dlvhdr/gh-dash) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31054372001) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Rich terminal UI for GitHub that doesn't break your flow |
| gh-lazy | 0.6.6 | [home](https://github.com/gizmo385/gh-lazy) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31129019194) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Terminal UI for interacting with GitHub |
| ghgrab | 2.0.2 | [home](https://github.com/abhixdd/ghgrab) | [2026-08-17](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32008206676) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Terminal tool to browse and download files in git forges |
| glaze | 8.2.0 | [home](https://github.com/stephenberry/glaze) | [2026-08-28](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33166775092) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Extremely fast, in memory, JSON and interface library for modern C++ |
| gofer | 0.5.1 | [home](https://codeberg.org/JakeAtLinux/Gofer) | [2026-08-28](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33210497767) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Fast, minimal application launcher written in pure Go. Supports both Way |
| gradle | 9.7.0 | [home](https://gradle.org) | [2026-08-15](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31854663050) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Build system for Java/C/C++ software |
| graphite-gtk-theme | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-all | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31077328663) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-black | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-black-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-compact-all | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31081919550) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-dark | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-dark-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-light | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-light-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-nord | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-nord-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-nord-dark | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-nord-dark-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-nord-light | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-nord-light-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| gum-panel | 2.0.0.001 | [home](https://codeberg.org/oSoWoSo/gum) | [2026-08-21](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32533946022) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Modified version of gum with panel support |
| helium-browser-bin | 0.16.6.1 | [home](https://helium.computer) | [2026-09-08](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34287372928) | ✅ | – | ✅ | – | zenobit | x86_64 aarch64 | Private, fast, and honest web browser based on Chromium (binary build) |
| hister | 0.19.0 | [home](https://github.com/asciimoo/hister) | [2026-09-04](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33862500692) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Your own search engine |
| hyprcursor | 0.1.13 | [home](https://github.com/hyprwm/hyprcursor) |  |  |  |  |  | zenobit |  | Hyprland cursor format, library and utilities |
| hyprdynamicmonitors | 1.4.0 | [home](https://github.com/fiffeek/hyprdynamicmonitors) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32546718482) | ❌ | ❌ | ❌ | ❌ | zenobit |  | Hyprland configuration based on connected displays, power and lid state |
| hyprgraphics | 0.3.0 | [home](https://github.com/hyprwm/hyprgraphics) |  |  |  |  |  | zenobit |  | Hyprland graphics resources and utilities |
| hypridle | 0.1.7 | [home](https://github.com/hyprwm/hypridle) |  |  |  |  |  | zenobit |  | Hyprland's idle daemon |
| hyprland | 0.52.1 | [home](https://hyprland.org/) |  |  |  |  |  | zenobit |  | Dynamic tiling Wayland compositor that doesn't sacrifice on its looks |
| hyprland-devel | 0.52.1 | [home](https://hyprland.org/) |  |  |  |  |  | zenobit |  | Dynamic tiling Wayland compositor that doesn't sacrifice on its looks |
| hyprland-guiutils | 0.1.0 | [home](https://github.com/hyprwm/hyprland-guiutils) |  |  |  |  |  | zenobit |  | Qt/QML utility apps for Hyprland |
| hyprland-protocols | 0.7.0 | [home](https://github.com/hyprwm/hyprland-protocols) |  |  |  |  |  | zenobit |  | Wayland protocol extensions for Hyprland |
| hyprland-qt-support | 0.1.0 | [home](https://github.com/hyprwm/hyprland-qt-support) |  |  |  |  |  | zenobit |  | QML style provider for Hypr* QT apps |
| hyprlang | 0.6.8 | [home](https://github.com/hyprwm/hyprlang) |  |  |  |  |  | zenobit |  | Official implementation library for the hypr config language |
| hyprlock | 0.9.2 | [home](https://github.com/hyprwm/hyprlock) |  |  |  |  |  | zenobit |  | Hyprland's GPU-accelerated screen locking utility |
| hyprmoncfg | 1.14.2 | [home](https://github.com/crmne/hyprmoncfg/) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32547176181) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Terminal-first monitor configurator and daemon for Hyprland |
| hyprpaper | 0.7.6 | [home](https://github.com/hyprwm/hyprpaper) |  |  |  |  |  | zenobit |  | Fast wallpaper utility for wlroots compositors with IPC controls |
| hyprpicker | 0.4.7 | [home](https://github.com/hyprwm/hyprpicker) |  |  |  |  |  | zenobit |  | Wlroots-compatible Wayland color picker that does not suck |
| hyprpolkitagent | 0.1.3 | [home](https://github.com/hyprwm/hyprpolkitagent) |  |  |  |  |  | zenobit |  | Simple polkit authentication agent for Hyprland, written in QT/QML |
| hyprsunset | 0.3.3 | [home](https://github.com/hyprwm/hyprsunset) |  |  |  |  |  | zenobit |  | Application to enable a blue-light filter on Hyprland |
| hyprsysteminfo | 0.1.3 | [home](https://github.com/hyprwm/hyprsysteminfo) |  |  |  |  |  | zenobit |  | Tiny qt6/qml application to display system informations |
| hyprtoolkit | 0.3.0 | [home](https://github.com/hyprwm/hyprtoolkit) |  |  |  |  |  | zenobit |  | Modern C++ Wayland-native GUI toolkit |
| hyprutils | 0.13.1 | [home](https://github.com/hyprwm/hyprutils) |  |  |  |  |  | zenobit |  | Hyprland utilities library used across the ecosystem |
| hyprwayland-scanner | 0.4.5 | [home](https://github.com/hyprwm/hyprwayland-scanner) |  |  |  |  |  | zenobit |  | Hyprland's implementation of wayland-scanner |
| kairo | 1.7.3 | [home](https://github.com/programmersd21/kairo) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31056045040) | ✅ | ✅ | ✅ | ✅ | nerdyslacker |  | Fast, keyboard-first terminal task manager |
| kando | 2.3.1 | [home](https://kando.menu) | [2026-09-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34307449867) | ✅ |  | ❌ |  | zenobit | x86_64 aarch64 | Do things with utmost efficiency |
| kmscon | 10.0.3 | [home](https://github.com/kmscon/kmscon) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34000695728) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Linux KMS/DRM based virtual Console Emulator |
| lazyrsync | 0.3.0 | [home](https://github.com/westpoint-io/lazyrsync) | [2026-08-15](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31875083533) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Friendly terminal UI for rsync |
| lemonade-server | 10.6.0 | [home](https://github.com/lemonade-sdk/lemonade) |  |  |  |  |  | zenobit |  | Local LLM Serving with GPU and NPU acceleration (Server) |
| lgogdownloader | 3.18 | [home](https://github.com/Sude-/lgogdownloader) | [2026-08-28](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33210420793) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Unofficial downloader to GOG.com for Linux users |
| libbtrfs | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| libbtrfs-devel | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| libbtrfsutil | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| libbtrfsutil-devel | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| libcprime | 5.0.1 | [home](https://gitlab.com/cubocore/libcprime) |  |  |  |  |  | zenobit |  | Library for bookmarking, saving activities, sharing files and more |
| librewolf-bin | 155.0.1.1 | [home](https://librewolf.net) | [2026-09-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34298159664) | ✅ |  | ✅ |  | zenobit | x86_64 aarch64 | Community-maintained fork of Firefox focused on privacy and security |
| libspng | 0.7.4 | [home](https://libspng.org/) |  |  |  |  |  | zenobit |  | Simple, modern libpng alternative |
| libtsm | 4.7.1 | [home](https://github.com/kmscon/libtsm) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34000695728) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Terminal-emulator State Machine |
| libtsm-devel | 4.7.1 | [home](https://github.com/kmscon/libtsm) |  |  |  |  |  | zenobit |  | Terminal-emulator State Machine |
| linuxcommandlibrary | 4.5.0 | [home](http://linuxcommandlibrary.com/) | [2026-08-15](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31864794409) | ✅ |  | ❌ |  | zenobit | x86_64 aarch64 | Linux reference app with basics, tips and formatted man pages |
| linuxcommandlibrary-desktop | 4.5.0 | [home](http://linuxcommandlibrary.com/) |  |  |  |  |  | zenobit | x86_64 aarch64 | Linux reference app with basics, tips and formatted man pages |
| llama.cpp | 10568 | [home](https://github.com/ggml-org/llama.cpp) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32541800300) | ❌ | ❌ | ✅ | ✅ | zenobit |  | LLM inference in C/C++ |
| llmfit | 1.1.14 | [home](https://github.com/AlexsJones/llmfit) | [2026-09-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33988217276) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Hundreds of models & providers, easy to find what fits your hardware |
| lunasvg | 3.5.0 | [home](https://github.com/sammycage/lunasvg) | [2026-08-13](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31753011465) | ✅ | ✅ | ✅ | ✅ | zenobit |  | SVG rendering and manipulation library in C++ |
| lunasvg-devel | 3.5.0 | [home](https://github.com/sammycage/lunasvg) |  |  |  |  |  | zenobit |  | SVG rendering and manipulation library in C++ |
| ly | 1.4.0 | [home](https://codeberg.org/fairyglade/ly) |  |  |  |  |  | zenobit | i686 x86_64 | Lightweight TUI (ncurses-like) display manager for Linux and BSD |
| lycan | 0.1.2 | [home](https://github.com/tutkuofnight/lycan) | [2026-08-14](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31845697273) | ✅ | ✅ |  |  | Bella109 | x86_64* | Lightweight PWA manager for Linux |
| menu-themes | 0.8.0 | [home](https://github.com/kando-menu/menu-themes) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31057950871) | ✅ | ❌ | ❌ | ❌ | zenobit |  | Collection of menu themes for Kando |
| mesa-amber | 26.1.2 | [home](https://www.mesa3d.org/) |  |  |  |  |  | Bella109 |  | Mesa for older hardware (legacy driver build) |
| nebula-gtk | 1.3.7 | [home](https://github.com/Letdown2491/nebula-gtk) | [2026-08-16](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31924899710) | ✅ | ✅ | ✅ | ✅ | zenobit |  | GTK frontend for Void Linux's XBPS tooling |
| NuvioDesktop | 0.3.5 | [home](https://github.com/blarns/NuvioForLinux) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32547730058) | ✅ | ❌ |  |  | Bella109 | x86_64* | Multi Media Hub - multiple sources for watching Series, Movies and Anime |
| nvchecker | 2.22 | [home](https://github.com/lilydjwg/nvchecker) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32541579783) | ✅ | ✅ | ✅ | ✅ | zenobit |  | New version checker for software releases |
| nwg-bar | 0.1.6 | [home](https://github.com/nwg-piotr/nwg-bar) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31011820913) | ✅ | ✅ | ✅ | ✅ | zenobit |  | GTK3-based button bar for wlroots-based compositors |
| nwg-clipman | 0.2.8 | [home](https://github.com/nwg-piotr/nwg-clipman) |  |  |  |  |  | zenobit |  | GTK based GUI for cliphist - nwg-shell clipboard manager |
| nwg-displays | 0.4.4 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-displays) | [2026-08-26](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32960837019) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Intuitive GUI to manage multiple displays for wayland |
| nwg-dock | 0.4.3 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-dock) |  |  |  |  |  | zenobit |  | GTK based dock for sway |
| nwg-dock-hyprland | 0.4.11 | [home](https://github.com/nwg-piotr/nwg-dock-hyprland) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31011820913) | ✅ | ✅ | ✅ | ✅ | zenobit |  | GTK3-based dock for Hyprland |
| nwg-drawer | 0.7.5 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-drawer) |  |  |  |  |  | zenobit |  | Application drawer for wlroots-based Wayland compositors |
| nwg-hello | 0.4.5 | [home](https://github.com/nwg-piotr/nwg-hello) |  |  |  |  |  | zenobit |  | GTK based greeter for greetd written in python |
| nwg-icon-picker | 0.1.1 | [home](https://github.com/nwg-piotr/nwg-icon-picker) |  |  |  |  |  | zenobit |  | GTK icon chooser with a text search option |
| nwg-menu | 0.1.9 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-menu) |  |  |  |  |  | zenobit |  | MenuStart plugin to nwg-panel, also capable of working standalone |
| nwg-panel | 0.10.15 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-panel) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31011820913) | ✅ | ✅ | ✅ | ✅ | zenobit |  | GTK based panel for sway and Hyprland Wayland compositors |
| nwg-readme-browser | 0.1.7 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-readme-browser) |  |  |  |  |  | zenobit |  | WebKitGTK based README file browser |
| nwg-shell | 0.5.50 | [home](https://nwg-piotr.github.io/nwg-shell) | [2026-08-26](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32961703884) | ✅ | ✅ | ✅ | ✅ | zenobit |  | GTK based shell for sway and Hyprland Wayland compositors |
| nwg-shell-config | 0.5.65 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-shell-config) | [2026-08-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31011820913) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Graphical user interface for configuring sway and Hyprland |
| nwg-shell-wallpapers | 1.5 | [home](https://github.com/nwg-piotr/nwg-shell-wallpapers) |  |  |  |  |  | zenobit |  | Selection of wallpapers contributed to the nwg-shell project |
| odin2 | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-clap | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-common | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-lv2 | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-standalone | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-vst3 | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| omniroute | 3.8.24 | [home](https://github.com/diegosouzapw/OmniRoute) | [2026-06-14](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/27488023509) | ✅ | ❌ | ❌ | ❌ | zenobit |  | Universal AI gateway with smart routing for multiple LLM providers |
| opencode | 1.18.30 | [home](https://github.com/anomalyco/opencode) | [2026-09-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34316835470) | ✅ | – | ✅ | – | zenobit | x86_64 aarch64 | Open source AI coding agent |
| patchance | 1.4.0 | [home](https://raysession.tuxfamily.org/) |  |  |  |  |  | Trve_AY |  | Jack patchbay GUI |
| pinguintv-installer-git | 0.0.0 | [home](https://pinguin-tv.de/installer.html) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31061281305) | ✅ |  |  |  | Bella109 | x86_64 | New GUI Installer for void |
| pop-fonts | 0.0.0 | [home](https://github.com/pop-os/fonts) |  |  |  |  |  | Bella109 |  | Pop Fonts |
| pop-icons | 3.5.1 | [home](https://github.com/pop-os/icon-theme) |  |  |  |  |  | Bella109 |  | TODO: pop-icons short_desc |
| pop-launcher | 1.8.0 | [home](https://github.com/pop-os/launcher) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34434395876) | ✅ | ✅ |  |  | zenobit | x86_64* | Modular IPC-based desktop launcher service |
| pop-sounds-theme | 5.5.1 | [home](https://github.com/pop-os/gtk-theme) |  |  |  |  |  | Bella109 |  | Pop sounds theme |
| proxelar | 0.5.1 | [home](https://github.com/emanuele-em/proxelar) | [2026-08-13](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31653257098) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Scriptable local traffic workbench |
| python3-anysqlite | 0.0.5 | [home](https://github.com/karpetrosyan/anysqlite) |  |  |  |  |  | zenobit |  | Provides interface to sqlite3 library and supports trio and asyncio |
| python3-geographiclib | 2.1 | [home](https://geographiclib.sourceforge.io/) |  |  |  |  |  | zenobit |  | Python implementation of the geodesic routines |
| python3-geopy | 2.4.1 | [home](https://github.com/geopy/geopy) |  |  |  |  |  | zenobit |  | Geocoding library for Python |
| python3-hishel | 1.1.9 | [home](https://github.com/karpetrosyan/hishel) |  |  |  |  |  | zenobit |  |  Elegant HTTP Caching for Python |
| python3-inline-snapshot | 0.32.6 | [home](https://15r10nk.github.io/inline-snapshot/latest) |  |  |  |  |  | zenobit |  | Boosts efficiency when writing tests |
| python3-linkify-it-py | 2.1.0 | [home](https://github.com/tsutsu3/linkify-it-py) |  |  |  |  |  | Orphaned |  | Linkify plugin for markdown-it-py |
| python3-PyGithub | 2.8.1 | [home](https://pygithub.readthedocs.io/) |  |  |  |  |  | Orphan |  | Python library to access the GitHub API v3 |
| python3-structlog | 26.1.0 | [home](https://github.com/hynek/structlog) | [2026-08-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31291129028) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Simple, powerful, and fast logging for Python |
| python3-textual | 5.3.0 | [home](https://textual.textualize.io) |  |  |  |  |  | icp |  | Modern Text User Interface framework |
| python3-uc-micro-py | 2.0.0 | [home](https://github.com/tsutsu3/uc.micro-py) |  |  |  |  |  | Orphaned |  | Unicode category micro library |
| qrunsvmgr | 0.2.5 | [home](https://codeberg.org/ItsZariep/qrunsvmgr) | [2026-08-15](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31872217404) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Service manager GUI (Qt6), supporting Runit and Dinit |
| quickemu | 4.9.9 | [home](https://github.com/quickemu-project/quickemu) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31061541051) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Quickly create and run optimised virtual machines |
| quickosdl | 0.3.2 | [home](https://github.com/lj3954/quickosdl) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31061541051) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Tool to quickly find URLs to images and download them |
| quickshell+ | 0.3.1 | [home](https://quickshell.org) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32562311819) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Flexible QtQuick-based desktop shell toolkit. Hyprland-enabled |
| radicle | 1.8.0 | [home](https://radicle.dev/) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31062331555) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Peer-to-peer code collaboration stack built on Git |
| raysession | 0.18.0 | [home](https://raysession.tuxfamily.org/) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31063545332) | ✅ | ✅ | ✅ | ✅ | Trve_AY |  | Session manager for audio programs using the NSM API |
| rebos | 3.5.2 | [home](https://gitlab.com/Oglo12/rebos) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34051058303) | ✅ | ✅ | ✅ | ✅ | zenobit |  | NixOS like repeatability for any Linux distribution |
| rgc | 1.2.0 | [home](https://github.com/flameshikari/rgc) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31064130903) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Rust alternative of grc |
| river-compositor | 0.4.8 | [home](https://codeberg.org/river/river) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34049764974) | ✅ | ✅ | ❌ | ❌ | LinuxNation | ~i686* ~armv6l* ~armv7l* | Non-monolithic tiling Wayland compositor |
| runkit | 1.4.0 | [home](https://github.com/Letdown2491/runkit) | [2026-08-16](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31924913048) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Graphical manager for runit services |
| rustdesk | 1.4.9 | [home](https://github.com/rustdesk/rustdesk) | [2026-07-01](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/28537315192) | ✅ | ❌ | – | – | Bella109 | x86_64* | Alternative to AnyDesk |
| sdkmanager | 0.7.0 | [home](https://gitlab.com/fdroid/sdkmanager) |  |  |  |  |  | zenobit |  | Drop-in replacement for Android sdkmanager written in Python |
| seamonkey-bin | 2.53.24 | [home](https://www.seamonkey-project.org/) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31127305333) | ✅ |  |  |  | zenobit | x86_64 | All-in-one internet application suite |
| sfizz-cli | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| sfizz-git | 1.2.3 | [home](https://sfztools.github.io/sfizz/) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31074232457) | ✅ | ✅ | ❌ | ❌ | Trve_AY |  | SFZ sampler |
| sfizz-lib | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| sfizz-lv2 | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| sfizz-vst3 | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| shattered-pixel-dungeon | 4.0.0 | [home](https://github.com/00-Evan/shattered-pixel-dungeon) | [2026-09-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34396576217) | ✅ | ❌ | ✅ | ❌ | zenobit |  | Open-source roguelike dungeon crawler with randomized levels and enemies |
| simplex-chat | 7.0.0 | [home](https://simplex.chat) | [2026-08-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31286208259) | ✅ | ✅ | ✅ | ❌ | rayfadh | ~i686 | Private and secure messaging application (CLI) |
| simplex-chat-desktop | 7.0.0 | [home](https://simplex.chat) |  |  |  |  |  | rayfadh | ~i686 | Private and secure messaging application (CLI) |
| surge-xt | 1.3.4 | [home](https://surge-synthesizer.github.io/) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31074214661) | ✅ | ✅ | ✅ | ❌ | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-clap | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-common | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-lv2 | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-standalone | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-vst3 | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| svi | 0.2.2 | [home](https://codeberg.org/LinuxNation/svi) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31065194979) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Graphical installer for Void Linux, built with GTK4 and Python |
| tdf | 0.5.0 | [home](https://github.com/itsjunetime/tdf) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31065892772) | ✅ | ✅ | ❌ | ❌ | zenobit |  | TUI PDF viewer |
| tiki | 0.6.1 | [home](https://github.com/boolean-maybe/tiki) |  |  |  |  |  | zenobit |  | Terminal Markdown-based shapeless workflow builder |
| tls-client | 1.15.1 | [home](https://github.com/bogdanfinn/tls-client) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31066153508) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Net/http.Client like HTTP Client |
| tomlplusplus | 3.4.0 | [home](https://marzer.github.io/tomlplusplus/) |  |  |  |  |  | zenobit |  | TOML config parser and serializer for C++ |
| tomlplusplus-devel | 3.4.0 | [home](https://marzer.github.io/tomlplusplus/) |  |  |  |  |  | zenobit |  | TOML config parser and serializer for C++ |
| Trilium | 0.105.0 | [home](https://github.com/TriliumNext/Trilium) | [2026-08-22](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/32546648839) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Build your personal knowledge base with Trilium Notes |
| tufw | 0.2.8 | [home](https://github.com/peltho/tufw) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31065594887) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Terminal UI for ufw |
| tuios | 0.7.0 | [home](https://github.com/Gaurav-Gosain/tuios) | [2026-09-07](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34116131850) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Terminal UI OS (Terminal Multiplexer) |
| tuisic | 2.5.2 | [home](https://github.com/Dark-Kernel/tuisic) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31065506428) | ✅ | ✅ | ✅ | ✅ | zenobit |  | TUI online music streaming application |
| typobuster | 1.0.0 | [home](https://github.com/nwg-piotr/typobuster) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31066955462) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Lightweight editor with text transformations and auto-correction |
| undelete-btrfs | 1.0 | [home](https://github.com/danthem/undelete-btrfs) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31068608970) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Undelete files in a BTRFS file system |
| vbm | 1.0.2 | [home](https://codeberg.org/oSoWoSo/vbm) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31084353246) | ❌ | ❌ | ❌ | ✅ | zenobit |  | XBPS package management helper for VoidLinux |
| vibepanel | 0.16.1 | [home](https://github.com/prankstr/vibepanel) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34046615244) | ✅ | ✅ | ✅ | ✅ | LinuxNation |  | GTK4 panel for Wayland with notifications, OSD, and quick settings |
| Vish | 1.1.3 | [home](https://github.com/Lluciocc/Vish) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31068750531) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Visual Scripting for Bash |
| vm-curator | 1.4.0 | [home](https://github.com/mroboff/vm-curator) | [2026-08-17](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31983802896) | ✅ | ✅ | ✅ | ✅ | zenobit |  | TUI to build and manage QEMU/KVM virtual machines |
| void-hardwaremanager-git | 0.0.0 | [home](https://codeberg.org/pinguin-void/Void-Driver-App) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31061986326) | ✅ |  | ✅ |  | zenobit | x86_64 aarch64 | Modern GTK4 setup tool for Void Linux |
| void-live-creator-git | 0.0.0 | [home](https://codeberg.org/pinguin-void/void-live-creator) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31070925394) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Create a live ISO from a running system |
| void-software-store | 1.9.4.02 | [home](https://codeberg.org/oSoWoSo/void-software-store) | [2026-06-14](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/27487508924) | ✅ | ✅ | ✅ | ✅ | zenobit |  | GUI Software Management |
| void-software-store-git | 999 | [home](https://codeberg.org/pinguin-void/void-software-store) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31070925394) | ✅ | ✅ | ✅ | ✅ | zenobit |  | GUI Software Management |
| void-src-builder-git | 0.0.0 | [home](https://codeberg.org/pinguin-void/void-src-builder) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31071408380) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Build packages from the Void source code |
| void-user-manager-git | 0.0.0 | [home](https://codeberg.org/pinguin-void/void-user-manager) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31071177363) | ✅ |  |  |  | zenobit | x86_64 | Modern, lightweight user and service management application |
| vote | 0.92 | [home](https://codeberg.org/oSoWoSo/vote) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31071543255) | ✅ | ✅ | ✅ | ✅ | zenobit |  | XBPS package management helper for VoidLinux |
| vtm | 2026.07.30 | [home](https://github.com/directvt/vtm) | [2026-08-13](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31659304324) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Text-based desktop environment |
| waterfox-bin | 6.7.2 | [home](https://www.waterfox.net) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34425981636) | ✅ |  | ✅ |  | zenobit | x86_64 aarch64 | Fast and private web browser |
| wpgtk | 6.7.1 | [home](https://github.com/deviantfero/wpgtk/) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31071774648) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Colorscheme, wallpaper and template manager for *nix |
| xdg-desktop-portal-cosmic | 1.8.0 | [home](https://github.com/pop-os/xdg-desktop-portal-cosmic) | [2026-09-10](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34428630431) | ✅ | ✅ | – | – | zenobit | x86_64* | Backend implementation for xdg-desktop-portal for COSMIC |
| xdg-desktop-portal-hyprland | 1.3.11 | [home](https://github.com/hyprwm/xdg-desktop-portal-hyprland) |  |  |  |  |  | zenobit |  | Backend of xdg-desktop-portal for Hyprland |
| xut | 0.4.2 | [home](https://codeberg.org/mobinmob/xut) | [2026-08-09](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31290589621) | ✅ | ✅ | ✅ | ✅ | mobinmob |  | Work with templates from unofficial repositories |
| xxtools-git | 0.0.0 | [home](https://github.com/Piraty/xxtools) | [2026-09-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/34003699024) | ✅ | ✅ | ✅ | ✅ | zenobit |  | Tools to ease packaging tasks for Void Linux |
| zen-browser-bin | 1.22b | [home](https://github.com/zen-browser/desktop) | [2026-09-05](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/33988529835) | ✅ |  | ✅ |  | Bella109 | x86_64 aarch64 | New Browser based on Firefox |
| zig | 0.16.0 | [home](https://ziglang.org) | [2026-08-06](https://github.com/oSoWoSo/Void_Community_Repository/actions/runs/31077263553) | ✅ | ✅ | ✅ | ❌ | Bella109 | x86_64* aarch64* | Programming language designed for robustness, optimality, and clarity |
