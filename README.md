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
| android-sdk | 36 | [home](https://developer.android.com/studio) |  |  |  |  |  | zenobit | x86_64 | Android SDK platform 36 and build-tools 29.0.3 |
| aquamarine | 0.15.0 | [home](https://github.com/hyprwm/aquamarine) |  |  |  |  |  | zenobit |  | Aquamarine is a very light linux rendering backend library |
| blocaled | 0.7 | [home](https://github.com/lfs-book/blocaled) |  |  |  |  |  | zenobit |  | Standalone implementation of the localed D-Bus service |
| brave-browser-bin | 1.94.121 | [home](https://www.brave.com/) |  |  |  |  |  | zenobit | x86_64 aarch64 | One of the most private browsers built on top off Chromium project |
| brave-origin-bin | 1.94.121 | [home](https://www.brave.com/) |  |  |  |  |  | zenobit | x86_64 aarc64 | Minimalist browser from the makers of Brave (binary) |
| brow6el | 0.3.5 | [home](https://brow6el.dev/) |  |  |  |  |  | zenobit | x86_64 | Minimalistic graphical terminal web browser using sixels |
| btrfs-progs | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| bulletty | 0.3.0 | [home](https://github.com/crocidb/bulletty) |  |  |  |  |  | zenobit |  | Feed reader for the terminal that stores the articles as Markdown |
| bun | 1.4.0 | [home](https://bun.sh) |  |  |  |  |  | zenobit | aarch64* x86_64* | JavaScript runtime, bundler, transpiler, and package manager |
| bun-bootstrap | 1.4.0 | [home](https://bun.sh) |  |  |  |  |  | zenobit | x86_64* aarch64* | Bootstrap package for bun (prebuilt binary) |
| caerus | 0.6.0 | [home](https://github.com/mendescotta/Caerus) |  |  |  |  |  | zenobit |  | Package manager for Void Linux, inspired by Synaptic |
| candy-icons-git | 0.11.1 | [home](https://www.opendesktop.org/p/1305251/) |  |  |  |  |  | Trve_AY |  | Sweet gradient icons, sweet rainbow folders included |
| cc-switch | 3.20.1 | [home](https://github.com/farion1231/cc-switch) |  |  |  |  |  | zenobit | x86_64* aarch64* | Assistant for Claude Code, Codex, OpenCode, OpenClaw & Gemini CLI |
| cliamp | 2.1.0 | [home](https://github.com/bjarneo/cliamp) |  |  |  |  |  | zenobit |  | Terminal music player inspired by winamp |
| clitest | 0.5.0 | [home](https://github.com/aureliojargas/clitest) |  |  |  |  |  | zenobit |  | Command Line Tester |
| Community-Repositories-Collection | 1 | [home](https://repo.osowoso.org) |  |  |  |  |  | zenobit |  | CRC: Collection of community repositories |
| corekeyboard | 5.0.1 | [home](https://gitlab.com/cubocore/coreapps/corekeyboard) |  |  |  |  |  | zenobit |  | X11 based virtual keyboard for C Suite |
| cosign | 3.1.3 | [home](https://github.com/sigstore/cosign) |  |  |  |  |  | zenobit |  | Code signing and transparency for containers and binaries |
| cosmic | 1.8.0 | [home](https://system76.com/cosmic) |  |  |  |  |  | zenobit | x86_64* | COSMIC meta-package for Void Linux |
| cosmic-applets | 1.8.0 | [home](https://github.com/pop-os/cosmic-applets) |  |  |  |  |  | zenobit | x86_64* | Applets for COSMIC Panel |
| cosmic-applibrary | 1.8.0 | [home](https://github.com/pop-os/cosmic-app-library) |  |  |  |  |  | zenobit | x86_64* | Application launcher for the COSMIC desktop |
| cosmic-bg | 1.8.0 | [home](https://github.com/pop-os/cosmic-bg) |  |  |  |  |  | zenobit | x86_64* | COSMIC session service which applies backgrounds to displays |
| cosmic-comp | 1.8.0 | [home](https://github.com/pop-os/cosmic-comp) |  |  |  |  |  | zenobit | x86_64* | Compositor for the COSMIC desktop environment |
| cosmic-desktop-full | 1.1.0 | [home](https://github.com/pop-os/cosmic-epoch) |  |  |  |  |  | Bella109 | x86_64* | Full Cosmic Desktop |
| cosmic-desktop-minimal | 1.1.0 | [home](https://github.com/pop-os/cosmic-epoch) |  |  |  |  |  | Bella109 | x86_64* | Meta Package for COSMIC Desktop |
| cosmic-edit | 1.8.0 | [home](https://github.com/pop-os/cosmic-edit) |  |  |  |  |  | zenobit | x86_64* | Text editor for the COSMIC desktop |
| cosmic-files | 1.8.0 | [home](https://github.com/pop-os/cosmic-files) |  |  |  |  |  | zenobit | x86_64* | File manager for the COSMIC desktop environment |
| cosmic-greeter | 1.8.0 | [home](https://github.com/pop-os/cosmic-greeter) |  |  |  |  |  | zenobit | x86_64* | COSMIC greeter for greetd |
| cosmic-icons | 1.8.0 | [home](https://github.com/pop-os/cosmic-icons) |  |  |  |  |  | zenobit | x86_64* | System76 Cosmic icon theme for Linux |
| cosmic-idle | 1.8.0 | [home](https://github.com/pop-os/cosmic-idle) |  |  |  |  |  | zenobit | x86_64* | Idle daemon for the COSMIC desktop |
| cosmic-initial-setup | 1.8.0 | [home](https://github.com/pop-os/cosmic-initial-setup) |  |  |  |  |  | zenobit | x86_64* | Initial setup for the COSMIC desktop |
| cosmic-launcher | 1.8.0 | [home](https://github.com/pop-os/cosmic-launcher) |  |  |  |  |  | zenobit | x86_64* | Layer Shell frontend for pop-launcher |
| cosmic-monitor | 1.8.0 | [home](https://github.com/pop-os/cosmic-monitor) |  |  |  |  |  | zenobit | x86_64* | System monitor for the COSMIC desktop |
| cosmic-notifications | 1.8.0 | [home](https://github.com/pop-os/cosmic-notifications) |  |  |  |  |  | zenobit | x86_64* | Layer Shell notifications daemon for the COSMIC desktop |
| cosmic-osd | 1.8.0 | [home](https://github.com/pop-os/cosmic-osd) |  |  |  |  |  | zenobit | x86_64* | On-Screen Display daemon for the COSMIC desktop |
| cosmic-panel | 1.8.0 | [home](https://github.com/pop-os/cosmic-panel) |  |  |  |  |  | zenobit | x86_64* | COSMIC applet for creating panels and docks |
| cosmic-player | 1.8.0 | [home](https://github.com/pop-os/cosmic-player) |  |  |  |  |  | zenobit | x86_64* | Media player for the COSMIC desktop |
| cosmic-randr | 1.8.0 | [home](https://github.com/pop-os/cosmic-randr) |  |  |  |  |  | zenobit | x86_64* | Library and utility for displaying and configuring Wayland outputs |
| cosmic-screenshot | 1.8.0 | [home](https://github.com/pop-os/cosmic-screenshot) |  |  |  |  |  | zenobit | x86_64* | Utility for capturing screenshots via XDG Desktop Portal |
| cosmic-session | 1.8.0 | [home](https://github.com/pop-os/cosmic-session) |  |  |  |  |  | zenobit | x86_64* | Session manager for the COSMIC desktop environment |
| cosmic-settings | 1.8.0 | [home](https://github.com/pop-os/cosmic-settings) |  |  |  |  |  | zenobit | x86_64* | Settings application for the COSMIC desktop environment |
| cosmic-settings-daemon | 1.8.0 | [home](https://github.com/pop-os/cosmic-settings-daemon) |  |  |  |  |  | zenobit | x86_64* | Settings daemon for the COSMIC desktop environment |
| cosmic-sound-theme | 1.8.0 | [home](https://github.com/pop-os/cosmic-sound-theme) |  |  |  |  |  | zenobit | x86_64* | Sound theme for the COSMIC desktop environment |
| cosmic-store | 1.8.0 | [home](https://github.com/pop-os/cosmic-store) |  |  |  |  |  | zenobit | x86_64* | Cosmic App Store |
| cosmic-term | 1.8.0 | [home](https://github.com/pop-os/cosmic-term) |  |  |  |  |  | zenobit | x86_64* | COSMIC terminal emulator |
| cosmic-tweaks | 0.2.2 | [home](https://github.com/cosmic-utils/cosmic-tweaks) |  |  |  |  |  | Bella109 | x86_64 | Tweaks for COSMIC |
| cosmic-wallpapers | 1.8.0 | [home](https://github.com/pop-os/cosmic-wallpapers) |  |  |  |  |  | zenobit | x86_64* | Wallpapers for the COSMIC Desktop Environment |
| cosmic-workspaces-epoch | 1.8.0 | [home](https://github.com/pop-os/cosmic-workspaces-epoch) |  |  |  |  |  | zenobit | x86_64* | COSMIC workspaces |
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
| crush | 0.90.0 | [home](https://github.com/charmbracelet/crush) |  |  |  |  |  | zenobit |  | Glamourous AI coding agent for your favourite terminal |
| cwal | 0.10.1 | [home](https://github.com/nitinbhat972/cwal) |  |  |  |  |  | zenobit |  | Blazing-fast pywal-like color palette generator written in C |
| dankcalendar | 1.6.1 | [home](https://github.com/AvengeMedia/dankcalendar) |  |  |  |  |  | zenobit |  | Calendar app for the Dank Linux desktop (Local, Google, CalDAV, iCloud) |
| DankMaterialShell | 1.5.3 | [home](https://github.com/AvengeMedia/DankMaterialShell) |  |  |  |  |  | zenobit |  | Desktop shell for wayland compositors built with Quickshell & GO |
| dashy | 4.1.5 | [home](https://github.com/Lissy93/dashy) |  |  |  |  |  | zenobit |  | Self-hostable personal dashboard |
| default-cursors | 1 | [home](https://www.voidlinux.org) |  |  |  |  |  | zenobit |  | Default cursor set |
| desktop-tui | 0.3.2 | [home](https://github.com/Julien-cpsn/desktop-tui) |  |  |  |  |  | zenobit |  | Desktop environment without graphics |
| devedeng | 4.22.1 | [home](https://www.rastersoft.com/programas/devede.html) |  |  |  |  |  | Bella109 |  | Create video DVDs and CDs |
| distrobox | 1.8.2.5 | [home](https://distrobox.it/) |  |  |  |  |  | zenobit |  | Podman/Docker wrapper to use any linux distribution in your terminal |
| dragonfly-reverb | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-clap | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-doc | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-lv2 | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-standalone | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-vst | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| dragonfly-reverb-vst3 | 3.2.10 | [home](https://michaelwillis.github.io/dragonfly-reverb) |  |  |  |  |  | Trve_AY |  | Collection of reverbs |
| drako | 0.3.3 | [home](https://github.com/lucky7xz/drako) |  |  |  |  |  | zenobit |  | Grid-based, customizable TUI-Deck launcher |
| easybashgui | 15.0.2 | [home](https://github.com/BashGui/easybashgui) |  |  |  |  |  | zenobit |  | Bash functions library that aims to give simple GUI functions |
| faugus-launcher | 2.2.2 | [home](https://github.com/Faugus/faugus-launcher) |  |  |  |  |  | zenobit |  | Simple and lightweight app for running Windows games using UMU-Launcher |
| fcitx5-lotus | 3.5.8 | [home](https://github.com/LotusInputMethod/fcitx5-lotus) |  |  |  |  |  | Coolllyn |  | Vietnamese input method for fcitx5 |
| fcitx5-lotus-settings | 3.5.8 | [home](https://github.com/LotusInputMethod/fcitx5-lotus) |  |  |  |  |  | Coolllyn |  | Vietnamese input method for fcitx5 |
| flyline | 1.7.1 | [home](https://github.com/HalFrgrd/flyline) |  |  |  |  |  | zenobit |  | Bash plugin to replace readline for a modern line editing experience |
| forgejo-runner | 13.1.0 | [home](https://code.forgejo.org/forgejo/runner) |  |  |  |  |  | zenobit |  | Continuous integration for Forgejo |
| FreeTube | 0.25.1 | [home](https://github.com/FreeTubeApp/FreeTube) |  |  |  |  |  | Bella109 | x86_64 | Client for watching YouTube Videos |
| ftxui | 7.0.3 | [home](https://github.com/ArthurSonzogni/FTXUI) |  |  |  |  |  | zenobit |  | C++ Functional Terminal User Interface |
| ftxui-devel | 7.0.3 | [home](https://github.com/ArthurSonzogni/FTXUI) |  |  |  |  |  | zenobit |  | C++ Functional Terminal User Interface |
| gama | 1.2.1 | [home](https://github.com/termkit/gama) |  |  |  |  |  | zenobit |  | Manage your GitHub Actions from Terminal with great UI |
| gh-dash | 4.25.2 | [home](https://github.com/dlvhdr/gh-dash) |  |  |  |  |  | zenobit |  | Rich terminal UI for GitHub that doesn't break your flow |
| gh-lazy | 0.6.6 | [home](https://github.com/gizmo385/gh-lazy) |  |  |  |  |  | zenobit |  | Terminal UI for interacting with GitHub |
| ghgrab | 2.0.2 | [home](https://github.com/abhixdd/ghgrab) |  |  |  |  |  | zenobit |  | Terminal tool to browse and download files in git forges |
| glaze | 8.3.0 | [home](https://github.com/stephenberry/glaze) |  |  |  |  |  | zenobit |  | Extremely fast, in memory, JSON and interface library for modern C++ |
| gofer | 0.5.1 | [home](https://codeberg.org/JakeAtLinux/Gofer) |  |  |  |  |  | zenobit |  | Fast, minimal application launcher written in pure Go. Supports both Way |
| gradle | 9.7.0 | [home](https://gradle.org) |  |  |  |  |  | zenobit |  | Build system for Java/C/C++ software |
| graphite-gtk-theme | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-all | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-black | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-black-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-compact | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
| graphite-gtk-theme-compact-all | 2025.07.06 | [home](https://github.com/vinceliuice/Graphite-gtk-theme) |  |  |  |  |  | zenobit |  | Material design inspired GTK theme with light and dark variants |
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
| gum-panel | 2.0.0.001 | [home](https://codeberg.org/oSoWoSo/gum) |  |  |  |  |  | zenobit |  | Modified version of gum with panel support |
| helium-browser-bin | 0.16.6.1 | [home](https://helium.computer) |  |  |  |  |  | zenobit | x86_64 aarch64 | Private, fast, and honest web browser based on Chromium (binary build) |
| hister | 0.19.0 | [home](https://github.com/asciimoo/hister) |  |  |  |  |  | zenobit |  | Your own search engine |
| hyprcursor | 0.1.13 | [home](https://github.com/hyprwm/hyprcursor) |  |  |  |  |  | zenobit |  | Hyprland cursor format, library and utilities |
| hyprdynamicmonitors | 1.4.0 | [home](https://github.com/fiffeek/hyprdynamicmonitors) |  |  |  |  |  | zenobit |  | Hyprland configuration based on connected displays, power and lid state |
| hyprgraphics | 0.5.1 | [home](https://github.com/hyprwm/hyprgraphics) |  |  |  |  |  | zenobit |  | Hyprland graphics resources and utilities |
| hypridle | 0.1.8 | [home](https://github.com/hyprwm/hypridle) |  |  |  |  |  | zenobit |  | Hyprland's idle daemon |
| hyprland | 0.56.2 | [home](https://hyprland.org/) |  |  |  |  |  | zenobit |  | Dynamic tiling Wayland compositor that doesn't sacrifice on its looks |
| hyprland-devel | 0.56.2 | [home](https://hyprland.org/) |  |  |  |  |  | zenobit |  | Dynamic tiling Wayland compositor that doesn't sacrifice on its looks |
| hyprland-guiutils | 0.2.2 | [home](https://github.com/hyprwm/hyprland-guiutils) |  |  |  |  |  | zenobit |  | Qt/QML utility apps for Hyprland |
| hyprland-protocols | 0.7.0 | [home](https://github.com/hyprwm/hyprland-protocols) |  |  |  |  |  | zenobit |  | Wayland protocol extensions for Hyprland |
| hyprland-qt-support | 0.1.0 | [home](https://github.com/hyprwm/hyprland-qt-support) |  |  |  |  |  | zenobit |  | QML style provider for Hypr* QT apps |
| hyprlang | 0.6.8 | [home](https://github.com/hyprwm/hyprlang) |  |  |  |  |  | zenobit |  | Official implementation library for the hypr config language |
| hyprlock | 0.9.6 | [home](https://github.com/hyprwm/hyprlock) |  |  |  |  |  | zenobit |  | Hyprland's GPU-accelerated screen locking utility |
| hyprmoncfg | 1.14.2 | [home](https://github.com/crmne/hyprmoncfg/) |  |  |  |  |  | zenobit |  | Terminal-first monitor configurator and daemon for Hyprland |
| hyprpaper | 0.8.4 | [home](https://github.com/hyprwm/hyprpaper) |  |  |  |  |  | zenobit |  | Fast wallpaper utility for wlroots compositors with IPC controls |
| hyprpicker | 0.4.7 | [home](https://github.com/hyprwm/hyprpicker) |  |  |  |  |  | zenobit |  | Wlroots-compatible Wayland color picker that does not suck |
| hyprpolkitagent | 0.2.0 | [home](https://github.com/hyprwm/hyprpolkitagent) |  |  |  |  |  | zenobit |  | Simple polkit authentication agent for Hyprland, written in QT/QML |
| hyprsunset | 0.4.0 | [home](https://github.com/hyprwm/hyprsunset) |  |  |  |  |  | zenobit |  | Application to enable a blue-light filter on Hyprland |
| hyprsysteminfo | 0.2.0 | [home](https://github.com/hyprwm/hyprsysteminfo) |  |  |  |  |  | zenobit |  | Tiny qt6/qml application to display system informations |
| hyprtoolkit | 0.6.0 | [home](https://github.com/hyprwm/hyprtoolkit) |  |  |  |  |  | zenobit |  | Modern C++ Wayland-native GUI toolkit |
| hyprutils | 0.14.2 | [home](https://github.com/hyprwm/hyprutils) |  |  |  |  |  | zenobit |  | Hyprland utilities library used across the ecosystem |
| hyprwayland-scanner | 0.4.6 | [home](https://github.com/hyprwm/hyprwayland-scanner) |  |  |  |  |  | zenobit |  | Hyprland's implementation of wayland-scanner |
| kairo | 1.7.3 | [home](https://github.com/programmersd21/kairo) |  |  |  |  |  | nerdyslacker |  | Fast, keyboard-first terminal task manager |
| kando | 2.3.1 | [home](https://kando.menu) |  |  |  |  |  | zenobit | x86_64 aarch64 | Do things with utmost efficiency |
| kmscon | 10.0.3 | [home](https://github.com/kmscon/kmscon) |  |  |  |  |  | zenobit |  | Linux KMS/DRM based virtual Console Emulator |
| lazyrsync | 0.3.0 | [home](https://github.com/westpoint-io/lazyrsync) |  |  |  |  |  | zenobit |  | Friendly terminal UI for rsync |
| lemonade-server | 10.6.0 | [home](https://github.com/lemonade-sdk/lemonade) |  |  |  |  |  | zenobit |  | Local LLM Serving with GPU and NPU acceleration (Server) |
| lgogdownloader | 3.18 | [home](https://github.com/Sude-/lgogdownloader) |  |  |  |  |  | zenobit |  | Unofficial downloader to GOG.com for Linux users |
| libbtrfs | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| libbtrfs-devel | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| libbtrfsutil | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| libbtrfsutil-devel | 7.1 | [home](https://btrfs.wiki.kernel.org/index.php/Main_Page) |  |  |  |  |  | Enno Boland |  | Btrfs filesystem utilities |
| libcprime | 5.0.1 | [home](https://gitlab.com/cubocore/libcprime) |  |  |  |  |  | zenobit |  | Library for bookmarking, saving activities, sharing files and more |
| librewolf-bin | 155.0.1.1 | [home](https://librewolf.net) |  |  |  |  |  | zenobit | x86_64 aarch64 | Community-maintained fork of Firefox focused on privacy and security |
| libspng | 0.7.4 | [home](https://libspng.org/) |  |  |  |  |  | zenobit |  | Simple, modern libpng alternative |
| libtsm | 4.7.1 | [home](https://github.com/kmscon/libtsm) |  |  |  |  |  | zenobit |  | Terminal-emulator State Machine |
| libtsm-devel | 4.7.1 | [home](https://github.com/kmscon/libtsm) |  |  |  |  |  | zenobit |  | Terminal-emulator State Machine |
| linuxcommandlibrary | 4.5.0 | [home](http://linuxcommandlibrary.com/) |  |  |  |  |  | zenobit | x86_64 aarch64 | Linux reference app with basics, tips and formatted man pages |
| linuxcommandlibrary-desktop | 4.5.0 | [home](http://linuxcommandlibrary.com/) |  |  |  |  |  | zenobit | x86_64 aarch64 | Linux reference app with basics, tips and formatted man pages |
| llama.cpp | 10568 | [home](https://github.com/ggml-org/llama.cpp) |  |  |  |  |  | zenobit |  | LLM inference in C/C++ |
| llmfit | 1.1.14 | [home](https://github.com/AlexsJones/llmfit) |  |  |  |  |  | zenobit |  | Hundreds of models & providers, easy to find what fits your hardware |
| lunasvg | 3.5.0 | [home](https://github.com/sammycage/lunasvg) |  |  |  |  |  | zenobit |  | SVG rendering and manipulation library in C++ |
| lunasvg-devel | 3.5.0 | [home](https://github.com/sammycage/lunasvg) |  |  |  |  |  | zenobit |  | SVG rendering and manipulation library in C++ |
| ly | 1.4.0 | [home](https://codeberg.org/fairyglade/ly) |  |  |  |  |  | zenobit | i686 x86_64 | Lightweight TUI (ncurses-like) display manager for Linux and BSD |
| lycan | 0.1.2 | [home](https://github.com/tutkuofnight/lycan) |  |  |  |  |  | Bella109 | x86_64* | Lightweight PWA manager for Linux |
| menu-themes | 0.8.0 | [home](https://github.com/kando-menu/menu-themes) |  |  |  |  |  | zenobit |  | Collection of menu themes for Kando |
| mesa-amber | 26.1.2 | [home](https://www.mesa3d.org/) |  |  |  |  |  | Bella109 |  | Mesa for older hardware (legacy driver build) |
| nebula-gtk | 1.3.7 | [home](https://github.com/Letdown2491/nebula-gtk) |  |  |  |  |  | zenobit |  | GTK frontend for Void Linux's XBPS tooling |
| NuvioDesktop | 0.3.5 | [home](https://github.com/blarns/NuvioForLinux) |  |  |  |  |  | Bella109 | x86_64* | Multi Media Hub - multiple sources for watching Series, Movies and Anime |
| nvchecker | 2.22 | [home](https://github.com/lilydjwg/nvchecker) |  |  |  |  |  | zenobit |  | New version checker for software releases |
| nwg-bar | 0.1.6 | [home](https://github.com/nwg-piotr/nwg-bar) |  |  |  |  |  | zenobit |  | GTK3-based button bar for wlroots-based compositors |
| nwg-clipman | 0.2.8 | [home](https://github.com/nwg-piotr/nwg-clipman) |  |  |  |  |  | zenobit |  | GTK based GUI for cliphist - nwg-shell clipboard manager |
| nwg-displays | 0.4.4 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-displays) |  |  |  |  |  | zenobit |  | Intuitive GUI to manage multiple displays for wayland |
| nwg-dock | 0.4.3 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-dock) |  |  |  |  |  | zenobit |  | GTK based dock for sway |
| nwg-dock-hyprland | 0.4.11 | [home](https://github.com/nwg-piotr/nwg-dock-hyprland) |  |  |  |  |  | zenobit |  | GTK3-based dock for Hyprland |
| nwg-drawer | 0.7.5 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-drawer) |  |  |  |  |  | zenobit |  | Application drawer for wlroots-based Wayland compositors |
| nwg-hello | 0.4.5 | [home](https://github.com/nwg-piotr/nwg-hello) |  |  |  |  |  | zenobit |  | GTK based greeter for greetd written in python |
| nwg-icon-picker | 0.1.1 | [home](https://github.com/nwg-piotr/nwg-icon-picker) |  |  |  |  |  | zenobit |  | GTK icon chooser with a text search option |
| nwg-menu | 0.1.9 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-menu) |  |  |  |  |  | zenobit |  | MenuStart plugin to nwg-panel, also capable of working standalone |
| nwg-panel | 0.10.15 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-panel) |  |  |  |  |  | zenobit |  | GTK based panel for sway and Hyprland Wayland compositors |
| nwg-readme-browser | 0.1.7 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-readme-browser) |  |  |  |  |  | zenobit |  | WebKitGTK based README file browser |
| nwg-shell | 0.5.50 | [home](https://nwg-piotr.github.io/nwg-shell) |  |  |  |  |  | zenobit |  | GTK based shell for sway and Hyprland Wayland compositors |
| nwg-shell-config | 0.5.65 | [home](https://nwg-piotr.github.io/nwg-shell/nwg-shell-config) |  |  |  |  |  | zenobit |  | Graphical user interface for configuring sway and Hyprland |
| nwg-shell-wallpapers | 1.5 | [home](https://github.com/nwg-piotr/nwg-shell-wallpapers) |  |  |  |  |  | zenobit |  | Selection of wallpapers contributed to the nwg-shell project |
| odin2 | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-clap | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-common | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-lv2 | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-standalone | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| odin2-vst3 | 2.4.1 | [home](https://thewavewarden.com/pages/odin-2) |  |  |  |  |  | Trve_AY |  | 24 voice polyphinic synthesizer with modulation and FX |
| omniroute | 3.8.24 | [home](https://github.com/diegosouzapw/OmniRoute) |  |  |  |  |  | zenobit |  | Universal AI gateway with smart routing for multiple LLM providers |
| opencode | 1.18.30 | [home](https://github.com/anomalyco/opencode) |  |  |  |  |  | zenobit | x86_64 aarch64 | Open source AI coding agent |
| patchance | 1.4.0 | [home](https://raysession.tuxfamily.org/) |  |  |  |  |  | Trve_AY |  | Jack patchbay GUI |
| pinguintv-installer-git | 0.0.0 | [home](https://pinguin-tv.de/installer.html) |  |  |  |  |  | Bella109 | x86_64 | New GUI Installer for void |
| pop-fonts | 0.0.0 | [home](https://github.com/pop-os/fonts) |  |  |  |  |  | Bella109 |  | Pop Fonts |
| pop-icons | 3.5.1 | [home](https://github.com/pop-os/icon-theme) |  |  |  |  |  | Bella109 |  | TODO: pop-icons short_desc |
| pop-launcher | 1.8.0 | [home](https://github.com/pop-os/launcher) |  |  |  |  |  | zenobit | x86_64* | Modular IPC-based desktop launcher service |
| pop-sounds-theme | 5.5.1 | [home](https://github.com/pop-os/gtk-theme) |  |  |  |  |  | Bella109 |  | Pop sounds theme |
| proxelar | 0.5.1 | [home](https://github.com/emanuele-em/proxelar) |  |  |  |  |  | zenobit |  | Scriptable local traffic workbench |
| python3-anysqlite | 0.0.5 | [home](https://github.com/karpetrosyan/anysqlite) |  |  |  |  |  | zenobit |  | Provides interface to sqlite3 library and supports trio and asyncio |
| python3-geographiclib | 2.1 | [home](https://geographiclib.sourceforge.io/) |  |  |  |  |  | zenobit |  | Python implementation of the geodesic routines |
| python3-geopy | 2.4.1 | [home](https://github.com/geopy/geopy) |  |  |  |  |  | zenobit |  | Geocoding library for Python |
| python3-hishel | 1.1.9 | [home](https://github.com/karpetrosyan/hishel) |  |  |  |  |  | zenobit |  |  Elegant HTTP Caching for Python |
| python3-inline-snapshot | 0.32.6 | [home](https://15r10nk.github.io/inline-snapshot/latest) |  |  |  |  |  | zenobit |  | Boosts efficiency when writing tests |
| python3-linkify-it-py | 2.1.0 | [home](https://github.com/tsutsu3/linkify-it-py) |  |  |  |  |  | Orphaned |  | Linkify plugin for markdown-it-py |
| python3-PyGithub | 2.8.1 | [home](https://pygithub.readthedocs.io/) |  |  |  |  |  | Orphan |  | Python library to access the GitHub API v3 |
| python3-structlog | 26.1.0 | [home](https://github.com/hynek/structlog) |  |  |  |  |  | zenobit |  | Simple, powerful, and fast logging for Python |
| python3-textual | 5.3.0 | [home](https://textual.textualize.io) |  |  |  |  |  | icp |  | Modern Text User Interface framework |
| python3-uc-micro-py | 2.0.0 | [home](https://github.com/tsutsu3/uc.micro-py) |  |  |  |  |  | Orphaned |  | Unicode category micro library |
| qrunsvmgr | 0.2.5 | [home](https://codeberg.org/ItsZariep/qrunsvmgr) |  |  |  |  |  | zenobit |  | Service manager GUI (Qt6), supporting Runit and Dinit |
| quickemu | 4.9.9 | [home](https://github.com/quickemu-project/quickemu) |  |  |  |  |  | zenobit |  | Quickly create and run optimised virtual machines |
| quickosdl | 0.3.2 | [home](https://github.com/lj3954/quickosdl) |  |  |  |  |  | zenobit |  | Tool to quickly find URLs to images and download them |
| quickshell+ | 0.3.1 | [home](https://quickshell.org) |  |  |  |  |  | zenobit |  | Flexible QtQuick-based desktop shell toolkit. Hyprland-enabled |
| radicle | 1.8.0 | [home](https://radicle.dev/) |  |  |  |  |  | zenobit |  | Peer-to-peer code collaboration stack built on Git |
| raysession | 0.18.0 | [home](https://raysession.tuxfamily.org/) |  |  |  |  |  | Trve_AY |  | Session manager for audio programs using the NSM API |
| rebos | 3.5.2 | [home](https://gitlab.com/Oglo12/rebos) |  |  |  |  |  | zenobit |  | NixOS like repeatability for any Linux distribution |
| rgc | 1.2.0 | [home](https://github.com/flameshikari/rgc) |  |  |  |  |  | zenobit |  | Rust alternative of grc |
| river-compositor | 0.4.8 | [home](https://codeberg.org/river/river) |  |  |  |  |  | LinuxNation | ~i686* ~armv6l* ~armv7l* | Non-monolithic tiling Wayland compositor |
| runkit | 1.4.0 | [home](https://github.com/Letdown2491/runkit) |  |  |  |  |  | zenobit |  | Graphical manager for runit services |
| rustdesk | 1.4.9 | [home](https://github.com/rustdesk/rustdesk) |  |  |  |  |  | Bella109 | x86_64* | Alternative to AnyDesk |
| sdbus-c++ | 2.3.1 | [home](https://github.com/Kistler-Group/sdbus-cpp) |  |  |  |  |  | Ly-sec |  | High-level C++ D-Bus library |
| sdkmanager | 0.7.0 | [home](https://gitlab.com/fdroid/sdkmanager) |  |  |  |  |  | zenobit |  | Drop-in replacement for Android sdkmanager written in Python |
| seamonkey-bin | 2.53.24 | [home](https://www.seamonkey-project.org/) |  |  |  |  |  | zenobit | x86_64 | All-in-one internet application suite |
| sfizz-cli | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| sfizz-git | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| sfizz-lib | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| sfizz-lv2 | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| sfizz-vst3 | 1.2.3 | [home](https://sfztools.github.io/sfizz/) |  |  |  |  |  | Trve_AY |  | SFZ sampler |
| shattered-pixel-dungeon | 4.0.0 | [home](https://github.com/00-Evan/shattered-pixel-dungeon) |  |  |  |  |  | zenobit |  | Open-source roguelike dungeon crawler with randomized levels and enemies |
| simplex-chat | 7.0.0 | [home](https://simplex.chat) |  |  |  |  |  | rayfadh | ~i686 | Private and secure messaging application (CLI) |
| simplex-chat-desktop | 7.0.0 | [home](https://simplex.chat) |  |  |  |  |  | rayfadh | ~i686 | Private and secure messaging application (CLI) |
| surge-xt | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-clap | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-common | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-lv2 | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-standalone | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| surge-xt-vst3 | 1.3.4 | [home](https://surge-synthesizer.github.io/) |  |  |  |  |  | Trve_AY |  | Subtractive hybrid synthesizer |
| svi | 0.2.2 | [home](https://codeberg.org/LinuxNation/svi) |  |  |  |  |  | zenobit |  | Graphical installer for Void Linux, built with GTK4 and Python |
| tdf | 0.5.0 | [home](https://github.com/itsjunetime/tdf) |  |  |  |  |  | zenobit |  | TUI PDF viewer |
| tiki | 0.6.1 | [home](https://github.com/boolean-maybe/tiki) |  |  |  |  |  | zenobit |  | Terminal Markdown-based shapeless workflow builder |
| tls-client | 1.15.1 | [home](https://github.com/bogdanfinn/tls-client) |  |  |  |  |  | zenobit |  | Net/http.Client like HTTP Client |
| tomlplusplus | 3.4.0 | [home](https://marzer.github.io/tomlplusplus/) |  |  |  |  |  | Cass Spencer |  | TOML config parser and serializer for C++ |
| tomlplusplus-devel | 3.4.0 | [home](https://marzer.github.io/tomlplusplus/) |  |  |  |  |  | Cass Spencer |  | TOML config parser and serializer for C++ |
| Trilium | 0.105.0 | [home](https://github.com/TriliumNext/Trilium) |  |  |  |  |  | zenobit |  | Build your personal knowledge base with Trilium Notes |
| tufw | 0.2.8 | [home](https://github.com/peltho/tufw) |  |  |  |  |  | zenobit |  | Terminal UI for ufw |
| tuios | 0.7.0 | [home](https://github.com/Gaurav-Gosain/tuios) |  |  |  |  |  | zenobit |  | Terminal UI OS (Terminal Multiplexer) |
| tuisic | 2.5.2 | [home](https://github.com/Dark-Kernel/tuisic) |  |  |  |  |  | zenobit |  | TUI online music streaming application |
| typobuster | 1.0.0 | [home](https://github.com/nwg-piotr/typobuster) |  |  |  |  |  | zenobit |  | Lightweight editor with text transformations and auto-correction |
| undelete-btrfs | 1.0 | [home](https://github.com/danthem/undelete-btrfs) |  |  |  |  |  | zenobit |  | Undelete files in a BTRFS file system |
| vbm | 1.0.2 | [home](https://codeberg.org/oSoWoSo/vbm) |  |  |  |  |  | zenobit |  | XBPS package management helper for VoidLinux |
| vibepanel | 0.16.1 | [home](https://github.com/prankstr/vibepanel) |  |  |  |  |  | LinuxNation |  | GTK4 panel for Wayland with notifications, OSD, and quick settings |
| Vish | 1.1.3 | [home](https://github.com/Lluciocc/Vish) |  |  |  |  |  | zenobit |  | Visual Scripting for Bash |
| vm-curator | 1.4.0 | [home](https://github.com/mroboff/vm-curator) |  |  |  |  |  | zenobit |  | TUI to build and manage QEMU/KVM virtual machines |
| void-hardwaremanager-git | 0.0.0 | [home](https://codeberg.org/pinguin-void/Void-Driver-App) |  |  |  |  |  | zenobit | x86_64 aarch64 | Modern GTK4 setup tool for Void Linux |
| void-live-creator-git | 0.0.0 | [home](https://codeberg.org/pinguin-void/void-live-creator) |  |  |  |  |  | zenobit |  | Create a live ISO from a running system |
| void-software-store | 1.9.4.02 | [home](https://codeberg.org/oSoWoSo/void-software-store) |  |  |  |  |  | zenobit |  | GUI Software Management |
| void-software-store-git | 999 | [home](https://codeberg.org/pinguin-void/void-software-store) |  |  |  |  |  | zenobit |  | GUI Software Management |
| void-src-builder-git | 0.0.0 | [home](https://codeberg.org/pinguin-void/void-src-builder) |  |  |  |  |  | zenobit |  | Build packages from the Void source code |
| void-user-manager-git | 0.0.0 | [home](https://codeberg.org/pinguin-void/void-user-manager) |  |  |  |  |  | zenobit | x86_64 | Modern, lightweight user and service management application |
| vote | 0.92 | [home](https://codeberg.org/oSoWoSo/vote) |  |  |  |  |  | zenobit |  | XBPS package management helper for VoidLinux |
| vtm | 2026.07.30 | [home](https://github.com/directvt/vtm) |  |  |  |  |  | zenobit |  | Text-based desktop environment |
| waterfox-bin | 6.7.2 | [home](https://www.waterfox.net) |  |  |  |  |  | zenobit | x86_64 aarch64 | Fast and private web browser |
| wpgtk | 6.7.1 | [home](https://github.com/deviantfero/wpgtk/) |  |  |  |  |  | zenobit |  | Colorscheme, wallpaper and template manager for *nix |
| xdg-desktop-portal-cosmic | 1.8.0 | [home](https://github.com/pop-os/xdg-desktop-portal-cosmic) |  |  |  |  |  | zenobit | x86_64* | Backend implementation for xdg-desktop-portal for COSMIC |
| xdg-desktop-portal-hyprland | 1.4.1 | [home](https://github.com/hyprwm/xdg-desktop-portal-hyprland) |  |  |  |  |  | zenobit |  | Backend of xdg-desktop-portal for Hyprland |
| xut | 0.4.2 | [home](https://codeberg.org/mobinmob/xut) |  |  |  |  |  | mobinmob |  | Work with templates from unofficial repositories |
| xxtools-git | 0.0.0 | [home](https://github.com/Piraty/xxtools) |  |  |  |  |  | zenobit |  | Tools to ease packaging tasks for Void Linux |
| zen-browser-bin | 1.22b | [home](https://github.com/zen-browser/desktop) |  |  |  |  |  | Bella109 | x86_64 aarch64 | New Browser based on Firefox |
| zig | 0.16.0 | [home](https://ziglang.org) |  |  |  |  |  | Bella109 | x86_64* aarch64* | Programming language designed for robustness, optimality, and clarity |
