
if jq ".DE" "/options.json" | grep -q "KDE Plasma (Heavy)"; then
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y dolphin \
    gwenview \
    kde-config-gtk-style \
    kdialog \
    kfind \
    khotkeys \
    kio-extras \
    knewstuff-dialog \
    konsole \
    ksystemstats \
    kwin-addons \
    kwin-x11 \
    kwrite \
    plasma-desktop \
    plasma-workspace \
    qml-module-qt-labs-platform \
    systemsettings
    sed -i 's/applications:org.kde.discover.desktop,/applications:org.kde.konsole.desktop,/g' /usr/share/plasma/plasmoids/org.kde.plasma.taskmanager/contents/config/main.xml
    cp /startwm-kde.sh /defaults/startwm.sh
fi
if jq ".DE" "/options.json" | grep -q "XFCE4 (Lightweight)"; then
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y firefox \
    mousepad \
    xfce4-terminal \
    xfce4 \
    xubuntu-default-settings \
    xubuntu-icon-theme
    rm -f /etc/xdg/autostart/xscreensaver.desktop
    cp /startwm-xfce.sh /defaults/startwm.sh
fi
if jq ".DE" "/options.json" | grep -q "I3 (Very Lightweight)"; then
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends firefox \
    i3 \
    i3-wm \
    stterm
    update-alternatives --set x-terminal-emulator /usr/bin/st
    cp /startwm-i3.sh /defaults/startwm.sh
fi
chmod +x /defaults/startwm.sh
rm /startwm-kde.sh /startwm-i3.sh /startwm-xfce.sh