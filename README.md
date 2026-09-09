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
| package | version | homepage | maintainer | notes |
|:--------|:--------|:---------|:-----------|:------|
| android-sdk | 36 | https://developer.android.com/studio | zenobit | x86_64 |
| aquamarine | 0.14.0 | https://github.com/hyprwm/aquamarine | zenobit |  |
| brave-browser-bin | 1.94.121 | https://www.brave.com/ | zenobit | x86_64 aarch64 |
| brave-origin-bin | 1.94.121 | https://www.brave.com/ | zenobit | x86_64 aarc64 |
| brow6el | 0.3.5 | https://brow6el.dev/ | zenobit | x86_64 |
| btrfs-progs | 7.1 | https://btrfs.wiki.kernel.org/index.php/Main_Page | Enno Boland |  |
| bulletty | 0.3.0 | https://github.com/crocidb/bulletty | zenobit |  |
| bun | 1.4.0 | https://bun.sh | zenobit | aarch64* x86_64* |
| bun-bootstrap | 1.4.0 | https://bun.sh | zenobit | x86_64* aarch64* |
| caerus | 0.6.0 | https://github.com/mendescotta/Caerus | zenobit |  |
| candy-icons-git | 0.11.1 | https://www.opendesktop.org/p/1305251/ | Trve_AY |  |
| cc-switch | 3.20.1 | https://github.com/farion1231/cc-switch | zenobit | x86_64* aarch64* |
| cliamp | 2.1.0 | https://github.com/bjarneo/cliamp | zenobit |  |
| clitest | 0.5.0 | https://github.com/aureliojargas/clitest | zenobit |  |
| Community-Repositories-Collection | 1 | https://repo.osowoso.org | zenobit |  |
| corekeyboard | 5.0.1 | https://gitlab.com/cubocore/coreapps/corekeyboard | zenobit |  |
| cosign | 3.1.3 | https://github.com/sigstore/cosign | zenobit |  |
| cosmic-applets | 1.1.0 | https://github.com/pop-os/cosmic-applets | Bella109 | x86_64* i686 |
| cosmic-applibrary | 1.1.0 | https://github.com/pop-os/cosmic-applibrary | Bella109 | x86_64* i686 |
| cosmic-bg | 1.1.0 | https://github.com/pop-os/cosmic-bg | Bella109 | x86_64* i686 |
| cosmic-comp | 1.1.0 | https://github.com/pop-os/cosmic-comp | Bella109 | x86_64* i686 |
| cosmic-desktop-full | 1.1.0 | https://github.com/pop-os/cosmic-epoch | Bella109 | x86_64* |
| cosmic-desktop-minimal | 1.1.0 | https://github.com/pop-os/cosmic-epoch | Bella109 | x86_64* |
| cosmic-edit | 1.1.0 | https://github.com/pop-os/cosmic-edit | Bella109 | x86_64* |
| cosmic-files | 1.1.0 | https://github.com/pop-os/cosmic-files | Bella109 | x86_64* |
| cosmic-greeter | 1.1.0 | https://github.com/pop-os/cosmic-greeter | Bella109 | x86_64* i686 |
| cosmic-icons | 1.1.0 | https://github.com/pop-os/cosmic-icons | Bella109 |  |
| cosmic-idle | 1.1.0 | https://github.com/pop-os/cosmic-idle | Bella109 | x86_64* i686 |
| cosmic-launcher | 1.1.0 | https://github.com/pop-os/cosmic-launcher | Bella109 | x86_64* i686 |
| cosmic-monitor | 1.1.0 | https://github.com/pop-os/cosmic-monitor | Bella109 | x86_64* |
| cosmic-notifications | 1.1.0 | https://github.com/pop-os/cosmic-notifications | Bella109 | x86_64* i686 |
| cosmic-osd | 1.1.0 | https://github.com/pop-os/cosmic-osd | Bella109 | x86_64* i686 |
| cosmic-panel | 1.1.0 | https://github.com/pop-os/cosmic-panel | Bella109 | x86_64* i686 |
| cosmic-player | 1.1.0 | https://github.com/pop-os/cosmic-player | Bella109 | x86_64* i686 |
| cosmic-randr | 1.1.0 | https://github.com/pop-os/cosmic-randr | Bella109 | x86_64* i686 |
| cosmic-screenshot | 1.1.0 | https://github.com/pop-os/cosmic-screenshot | Bella109 | x86_64* i686 |
| cosmic-session | 1.1.0 | https://github.com/pop-os/cosmic-session | Bella109 | x86_64* i686 |
| cosmic-settings | 1.1.0 | https://github.com/pop-os/cosmic-settings | Bella109 | x86_64* i686 |
| cosmic-settings-daemon | 1.1.0 | https://github.com/pop-os/cosmic-settings-daemon | Bella109 | x86_64* i686 |
| cosmic-term | 1.1.0 | https://github.com/pop-os/cosmic-term | Bella109 | x86_64* |
| cosmic-tweaks | 0.2.2 | https://github.com/cosmic-utils/cosmic-tweaks | Bella109 | x86_64 |
| cosmic-wallpapers | 1.1.0 | https://github.com/pop-os/cosmic-wallpapers | Bella109 |  |
| cosmic-workspaces-epoch | 1.1.0 | https://github.com/pop-os/cosmic-workspaces-epoch | Bella109 | x86_64* i686 |
| CRC-black-hole | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-brgvos | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-cereus-core | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-cereus-extra | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-cosmic | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-d77void | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-hyprland | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-jake | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-lazy | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-librewolf | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-noid | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-odyssey | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-sofijacom | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-sonicde | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-split | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-voiders | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-vostock | 1 | https://repo.osowoso.org | zenobit |  |
| CRC-xlibre | 1 | https://repo.osowoso.org | zenobit |  |
| crush | 0.90.0 | https://github.com/charmbracelet/crush | zenobit |  |
| cwal | 0.10.1 | https://github.com/nitinbhat972/cwal | zenobit |  |
| dankcalendar | 1.6.1 | https://github.com/AvengeMedia/dankcalendar | zenobit |  |
| DankMaterialShell | 1.5.3 | https://github.com/AvengeMedia/DankMaterialShell | zenobit |  |
| dashy | 4.1.5 | https://github.com/Lissy93/dashy | zenobit |  |
| desktop-tui | 0.3.2 | https://github.com/Julien-cpsn/desktop-tui | zenobit |  |
| devedeng | 4.22.1 | https://www.rastersoft.com/programas/devede.html | Bella109 |  |
| distrobox | 1.8.2.5 | https://distrobox.it/ | zenobit |  |
| dragonfly-reverb | 3.2.10 | https://michaelwillis.github.io/dragonfly-reverb | Trve_AY |  |
| dragonfly-reverb-clap | 3.2.10 | https://michaelwillis.github.io/dragonfly-reverb | Trve_AY |  |
| dragonfly-reverb-doc | 3.2.10 | https://michaelwillis.github.io/dragonfly-reverb | Trve_AY |  |
| dragonfly-reverb-lv2 | 3.2.10 | https://michaelwillis.github.io/dragonfly-reverb | Trve_AY |  |
| dragonfly-reverb-standalone | 3.2.10 | https://michaelwillis.github.io/dragonfly-reverb | Trve_AY |  |
| dragonfly-reverb-vst | 3.2.10 | https://michaelwillis.github.io/dragonfly-reverb | Trve_AY |  |
| dragonfly-reverb-vst3 | 3.2.10 | https://michaelwillis.github.io/dragonfly-reverb | Trve_AY |  |
| drako | 0.3.3 | https://github.com/lucky7xz/drako | zenobit |  |
| easybashgui | 15.0.2 | https://github.com/BashGui/easybashgui | zenobit |  |
| faugus-launcher | 2.2.2 | https://github.com/Faugus/faugus-launcher | zenobit |  |
| fcitx5-lotus | 3.5.8 | https://github.com/LotusInputMethod/fcitx5-lotus | Coolllyn |  |
| fcitx5-lotus-settings | 3.5.8 | https://github.com/LotusInputMethod/fcitx5-lotus | Coolllyn |  |
| flyline | 1.7.1 | https://github.com/HalFrgrd/flyline | zenobit |  |
| forgejo-runner | 13.1.0 | https://code.forgejo.org/forgejo/runner | zenobit |  |
| FreeTube | 0.25.1 | https://github.com/FreeTubeApp/FreeTube | Bella109 | x86_64 |
| ftxui | 7.0.3 | https://github.com/ArthurSonzogni/FTXUI | zenobit |  |
| ftxui-devel | 7.0.3 | https://github.com/ArthurSonzogni/FTXUI | zenobit |  |
| gama | 1.2.1 | https://github.com/termkit/gama | zenobit |  |
| gh-dash | 4.25.2 | https://github.com/dlvhdr/gh-dash | zenobit |  |
| gh-lazy | 0.6.6 | https://github.com/gizmo385/gh-lazy | zenobit |  |
| ghgrab | 2.0.2 | https://github.com/abhixdd/ghgrab | zenobit |  |
| glaze | 8.2.0 | https://github.com/stephenberry/glaze | zenobit |  |
| gofer | 0.5.1 | https://codeberg.org/JakeAtLinux/Gofer | zenobit |  |
| gradle | 9.7.0 | https://gradle.org | zenobit |  |
| graphite-gtk-theme | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-all | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-black | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-black-compact | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-compact | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-compact-all | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-dark | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-dark-compact | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-light | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-light-compact | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-nord | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-nord-compact | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-nord-dark | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-nord-dark-compact | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-nord-light | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| graphite-gtk-theme-nord-light-compact | 2025.07.06 | https://github.com/vinceliuice/Graphite-gtk-theme | zenobit |  |
| gum-panel | 2.0.0.001 | https://codeberg.org/oSoWoSo/gum | zenobit |  |
| helium-browser-bin | 0.16.6.1 | https://helium.computer | zenobit | x86_64 aarch64 |
| hister | 0.19.0 | https://github.com/asciimoo/hister | zenobit |  |
| hyprcursor | 0.1.13 | https://github.com/hyprwm/hyprcursor | zenobit |  |
| hyprdynamicmonitors | 1.4.0 | https://github.com/fiffeek/hyprdynamicmonitors | zenobit |  |
| hyprgraphics | 0.3.0 | https://github.com/hyprwm/hyprgraphics | zenobit |  |
| hypridle | 0.1.7 | https://github.com/hyprwm/hypridle | zenobit |  |
| hyprland | 0.52.1 | https://hyprland.org/ | zenobit |  |
| hyprland-devel | 0.52.1 | https://hyprland.org/ | zenobit |  |
| hyprland-guiutils | 0.1.0 | https://github.com/hyprwm/hyprland-guiutils | zenobit |  |
| hyprland-protocols | 0.7.0 | https://github.com/hyprwm/hyprland-protocols | zenobit |  |
| hyprland-qt-support | 0.1.0 | https://github.com/hyprwm/hyprland-qt-support | zenobit |  |
| hyprlang | 0.6.8 | https://github.com/hyprwm/hyprlang | zenobit |  |
| hyprlock | 0.9.2 | https://github.com/hyprwm/hyprlock | zenobit |  |
| hyprmoncfg | 1.14.2 | https://github.com/crmne/hyprmoncfg/ | zenobit |  |
| hyprpaper | 0.7.6 | https://github.com/hyprwm/hyprpaper | zenobit |  |
| hyprpicker | 0.4.7 | https://github.com/hyprwm/hyprpicker | zenobit |  |
| hyprpolkitagent | 0.1.3 | https://github.com/hyprwm/hyprpolkitagent | zenobit |  |
| hyprsunset | 0.3.3 | https://github.com/hyprwm/hyprsunset | zenobit |  |
| hyprsysteminfo | 0.1.3 | https://github.com/hyprwm/hyprsysteminfo | zenobit |  |
| hyprtoolkit | 0.3.0 | https://github.com/hyprwm/hyprtoolkit | zenobit |  |
| hyprutils | 0.13.1 | https://github.com/hyprwm/hyprutils | zenobit |  |
| hyprwayland-scanner | 0.4.5 | https://github.com/hyprwm/hyprwayland-scanner | zenobit |  |
| kairo | 1.7.3 | https://github.com/programmersd21/kairo | nerdyslacker |  |
| kando | 2.3.1 | https://kando.menu | zenobit | x86_64 aarch64 |
| kmscon | 10.0.3 | https://github.com/kmscon/kmscon | zenobit |  |
| lazyrsync | 0.3.0 | https://github.com/westpoint-io/lazyrsync | zenobit |  |
| lemonade-server | 10.6.0 | https://github.com/lemonade-sdk/lemonade | zenobit |  |
| lgogdownloader | 3.18 | https://github.com/Sude-/lgogdownloader | zenobit |  |
| libbtrfs | 7.1 | https://btrfs.wiki.kernel.org/index.php/Main_Page | Enno Boland |  |
| libbtrfs-devel | 7.1 | https://btrfs.wiki.kernel.org/index.php/Main_Page | Enno Boland |  |
| libbtrfsutil | 7.1 | https://btrfs.wiki.kernel.org/index.php/Main_Page | Enno Boland |  |
| libbtrfsutil-devel | 7.1 | https://btrfs.wiki.kernel.org/index.php/Main_Page | Enno Boland |  |
| libcprime | 5.0.1 | https://gitlab.com/cubocore/libcprime | zenobit |  |
| librewolf-bin | 155.0.1.1 | https://librewolf.net | zenobit | x86_64 aarch64 |
| libspng | 0.7.4 | https://libspng.org/ | zenobit |  |
| libtsm | 4.7.1 | https://github.com/kmscon/libtsm | zenobit |  |
| libtsm-devel | 4.7.1 | https://github.com/kmscon/libtsm | zenobit |  |
| linuxcommandlibrary | 4.5.0 | http://linuxcommandlibrary.com/ | zenobit | x86_64 aarch64 |
| linuxcommandlibrary-desktop | 4.5.0 | http://linuxcommandlibrary.com/ | zenobit | x86_64 aarch64 |
| llama.cpp | 10568 | https://github.com/ggml-org/llama.cpp | zenobit |  |
| llmfit | 1.1.14 | https://github.com/AlexsJones/llmfit | zenobit |  |
| lunasvg | 3.5.0 | https://github.com/sammycage/lunasvg | zenobit |  |
| lunasvg-devel | 3.5.0 | https://github.com/sammycage/lunasvg | zenobit |  |
| ly | 1.4.0 | https://codeberg.org/fairyglade/ly | zenobit | i686 x86_64 |
| lycan | 0.1.2 | https://github.com/tutkuofnight/lycan | Bella109 | x86_64* |
| menu-themes | 0.8.0 | https://github.com/kando-menu/menu-themes | zenobit |  |
| mesa-amber | 26.1.2 | https://www.mesa3d.org/ | Bella109 |  |
| nebula-gtk | 1.3.7 | https://github.com/Letdown2491/nebula-gtk | zenobit |  |
| NuvioDesktop | 0.3.5 | https://github.com/blarns/NuvioForLinux | Bella109 | x86_64* |
| nvchecker | 2.22 | https://github.com/lilydjwg/nvchecker | zenobit |  |
| nwg-bar | 0.1.6 | https://github.com/nwg-piotr/nwg-bar | zenobit |  |
| nwg-clipman | 0.2.8 | https://github.com/nwg-piotr/nwg-clipman | zenobit |  |
| nwg-displays | 0.4.4 | https://nwg-piotr.github.io/nwg-shell/nwg-displays | zenobit |  |
| nwg-dock | 0.4.3 | https://nwg-piotr.github.io/nwg-shell/nwg-dock | zenobit |  |
| nwg-dock-hyprland | 0.4.11 | https://github.com/nwg-piotr/nwg-dock-hyprland | zenobit |  |
| nwg-drawer | 0.7.5 | https://nwg-piotr.github.io/nwg-shell/nwg-drawer | zenobit |  |
| nwg-hello | 0.4.5 | https://github.com/nwg-piotr/nwg-hello | zenobit |  |
| nwg-icon-picker | 0.1.1 | https://github.com/nwg-piotr/nwg-icon-picker | zenobit |  |
| nwg-menu | 0.1.9 | https://nwg-piotr.github.io/nwg-shell/nwg-menu | zenobit |  |
| nwg-panel | 0.10.15 | https://nwg-piotr.github.io/nwg-shell/nwg-panel | zenobit |  |
| nwg-readme-browser | 0.1.7 | https://nwg-piotr.github.io/nwg-shell/nwg-readme-browser | zenobit |  |
| nwg-shell | 0.5.50 | https://nwg-piotr.github.io/nwg-shell | zenobit |  |
| nwg-shell-config | 0.5.65 | https://nwg-piotr.github.io/nwg-shell/nwg-shell-config | zenobit |  |
| nwg-shell-wallpapers | 1.5 | https://github.com/nwg-piotr/nwg-shell-wallpapers | zenobit |  |
| odin2 | 2.4.1 | https://thewavewarden.com/pages/odin-2 | Trve_AY |  |
| odin2-clap | 2.4.1 | https://thewavewarden.com/pages/odin-2 | Trve_AY |  |
| odin2-common | 2.4.1 | https://thewavewarden.com/pages/odin-2 | Trve_AY |  |
| odin2-lv2 | 2.4.1 | https://thewavewarden.com/pages/odin-2 | Trve_AY |  |
| odin2-standalone | 2.4.1 | https://thewavewarden.com/pages/odin-2 | Trve_AY |  |
| odin2-vst3 | 2.4.1 | https://thewavewarden.com/pages/odin-2 | Trve_AY |  |
| omniroute | 3.8.24 | https://github.com/diegosouzapw/OmniRoute | zenobit |  |
| opencode | 1.18.30 | https://github.com/anomalyco/opencode | zenobit | x86_64 aarch64 |
| patchance | 1.4.0 | https://raysession.tuxfamily.org/ | Trve_AY |  |
| pinguintv-installer-git | 0.0.0 | https://pinguin-tv.de/installer.html | Bella109 | x86_64 |
| pop-fonts | 0.0.0 | https://github.com/pop-os/fonts | Bella109 |  |
| pop-icons | 3.5.1 | https://github.com/pop-os/icon-theme | Bella109 |  |
| pop-launcher | 1.2.7 | https://github.com/pop-os/launcher | Bella109 | x86_64* i686 |
| pop-sounds-theme | 5.5.1 | https://github.com/pop-os/gtk-theme | Bella109 |  |
| proxelar | 0.5.1 | https://github.com/emanuele-em/proxelar | zenobit |  |
| python3-anysqlite | 0.0.5 | https://github.com/karpetrosyan/anysqlite | zenobit |  |
| python3-geographiclib | 2.1 | https://geographiclib.sourceforge.io/ | zenobit |  |
| python3-geopy | 2.4.1 | https://github.com/geopy/geopy | zenobit |  |
| python3-hishel | 1.1.9 | https://github.com/karpetrosyan/hishel | zenobit |  |
| python3-inline-snapshot | 0.32.6 | https://15r10nk.github.io/inline-snapshot/latest | zenobit |  |
| python3-linkify-it-py | 2.1.0 | https://github.com/tsutsu3/linkify-it-py | Orphaned |  |
| python3-PyGithub | 2.8.1 | https://pygithub.readthedocs.io/ | Orphan |  |
| python3-structlog | 26.1.0 | https://github.com/hynek/structlog | zenobit |  |
| python3-textual | 5.3.0 | https://textual.textualize.io | icp |  |
| python3-uc-micro-py | 2.0.0 | https://github.com/tsutsu3/uc.micro-py | Orphaned |  |
| qrunsvmgr | 0.2.5 | https://codeberg.org/ItsZariep/qrunsvmgr | zenobit |  |
| quickemu | 4.9.9 | https://github.com/quickemu-project/quickemu | zenobit |  |
| quickosdl | 0.3.2 | https://github.com/lj3954/quickosdl | zenobit |  |
| quickshell+ | 0.3.1 | https://quickshell.org | zenobit |  |
| radicle | 1.8.0 | https://radicle.dev/ | zenobit |  |
| raysession | 0.18.0 | https://raysession.tuxfamily.org/ | Trve_AY |  |
| rebos | 3.5.2 | https://gitlab.com/Oglo12/rebos | zenobit |  |
| rgc | 1.2.0 | https://github.com/flameshikari/rgc | zenobit |  |
| river-compositor | 0.4.8 | https://codeberg.org/river/river | LinuxNation | ~i686* ~armv6l* ~armv7l* |
| runkit | 1.4.0 | https://github.com/Letdown2491/runkit | zenobit |  |
| rustdesk | 1.4.9 | https://github.com/rustdesk/rustdesk | Bella109 | x86_64* |
| sdkmanager | 0.7.0 | https://gitlab.com/fdroid/sdkmanager | zenobit |  |
| seamonkey-bin | 2.53.24 | https://www.seamonkey-project.org/ | zenobit | x86_64 |
| sfizz-cli | 1.2.3 | https://sfztools.github.io/sfizz/ | Trve_AY |  |
| sfizz-git | 1.2.3 | https://sfztools.github.io/sfizz/ | Trve_AY |  |
| sfizz-lib | 1.2.3 | https://sfztools.github.io/sfizz/ | Trve_AY |  |
| sfizz-lv2 | 1.2.3 | https://sfztools.github.io/sfizz/ | Trve_AY |  |
| sfizz-vst3 | 1.2.3 | https://sfztools.github.io/sfizz/ | Trve_AY |  |
| shattered-pixel-dungeon | 4.0.0 | https://github.com/00-Evan/shattered-pixel-dungeon | zenobit |  |
| simplex-chat | 7.0.0 | https://simplex.chat | rayfadh | ~i686 |
| simplex-chat-desktop | 7.0.0 | https://simplex.chat | rayfadh | ~i686 |
| surge-xt | 1.3.4 | https://surge-synthesizer.github.io/ | Trve_AY |  |
| surge-xt-clap | 1.3.4 | https://surge-synthesizer.github.io/ | Trve_AY |  |
| surge-xt-common | 1.3.4 | https://surge-synthesizer.github.io/ | Trve_AY |  |
| surge-xt-lv2 | 1.3.4 | https://surge-synthesizer.github.io/ | Trve_AY |  |
| surge-xt-standalone | 1.3.4 | https://surge-synthesizer.github.io/ | Trve_AY |  |
| surge-xt-vst3 | 1.3.4 | https://surge-synthesizer.github.io/ | Trve_AY |  |
| svi | 0.2.2 | https://codeberg.org/LinuxNation/svi | zenobit |  |
| tdf | 0.5.0 | https://github.com/itsjunetime/tdf | zenobit |  |
| tiki | 0.6.1 | https://github.com/boolean-maybe/tiki | zenobit |  |
| tls-client | 1.15.1 | https://github.com/bogdanfinn/tls-client | zenobit |  |
| tomlplusplus | 3.4.0 | https://marzer.github.io/tomlplusplus/ | zenobit |  |
| tomlplusplus-devel | 3.4.0 | https://marzer.github.io/tomlplusplus/ | zenobit |  |
| Trilium | 0.105.0 | https://github.com/TriliumNext/Trilium | zenobit |  |
| tufw | 0.2.8 | https://github.com/peltho/tufw | zenobit |  |
| tuios | 0.7.0 | https://github.com/Gaurav-Gosain/tuios | zenobit |  |
| tuisic | 2.5.2 | https://github.com/Dark-Kernel/tuisic | zenobit |  |
| typobuster | 1.0.0 | https://github.com/nwg-piotr/typobuster | zenobit |  |
| undelete-btrfs | 1.0 | https://github.com/danthem/undelete-btrfs | zenobit |  |
| vbm | 1.0.2 | https://codeberg.org/oSoWoSo/vbm | zenobit |  |
| vibepanel | 0.16.1 | https://github.com/prankstr/vibepanel | LinuxNation |  |
| Vish | 1.1.3 | https://github.com/Lluciocc/Vish | zenobit |  |
| vm-curator | 1.4.0 | https://github.com/mroboff/vm-curator | zenobit |  |
| void-hardwaremanager-git | 0.0.0 | https://codeberg.org/pinguin-void/Void-Driver-App | zenobit | x86_64 aarch64 |
| void-live-creator-git | 0.0.0 | https://codeberg.org/pinguin-void/void-live-creator | zenobit |  |
| void-software-store | 1.9.4.02 | https://codeberg.org/oSoWoSo/void-software-store | zenobit |  |
| void-software-store-git | 999 | https://codeberg.org/pinguin-void/void-software-store | zenobit |  |
| void-src-builder-git | 0.0.0 | https://codeberg.org/pinguin-void/void-src-builder | zenobit |  |
| void-user-manager-git | 0.0.0 | https://codeberg.org/pinguin-void/void-user-manager | zenobit | x86_64 |
| vote | 0.92 | https://codeberg.org/oSoWoSo/vote | zenobit |  |
| vtm | 2026.07.30 | https://github.com/directvt/vtm | zenobit |  |
| waterfox-bin | 6.7.2 | https://www.waterfox.net | zenobit | x86_64 aarch64 |
| wpgtk | 6.7.1 | https://github.com/deviantfero/wpgtk/ | zenobit |  |
| xdg-desktop-portal-cosmic | 1.1.0 | https://github.com/pop-os/xdg-desktop-portal-cosmic | Bella109 | x86_64* |
| xdg-desktop-portal-hyprland | 1.3.11 | https://github.com/hyprwm/xdg-desktop-portal-hyprland | zenobit |  |
| xut | 0.4.2 | https://codeberg.org/mobinmob/xut | mobinmob |  |
| xxtools-git | 0.0.0 | https://github.com/Piraty/xxtools | zenobit |  |
| zen-browser-bin | 1.22b | https://github.com/zen-browser/desktop | Bella109 | x86_64 aarch64 |
| zig | 0.16.0 | https://ziglang.org | Bella109 | x86_64* aarch64* |
