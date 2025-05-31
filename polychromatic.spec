Name: polychromatic
Version: 0.9.4
Release: 1
Summary: RGB lighting management front-end application for OpenRazer
Group:  System/Configuration/Other
License: GPL-3.0
URL: https://github.com/polychromatic/polychromatic
Source0: https://github.com/polychromatic/polychromatic/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: rsync
BuildRequires: python
BuildRequires: sassc
BuildRequires: intltool
BuildRequires: meson

Requires: python
Requires: python-colorama
Requires: python-colour
Requires: python-setproctitle
Requires: python-requests
Requires: python-openrazer
Requires: python-qt6
Requires: %{_lib}Qt6Svg
Requires: python-qt6-webengine
Requires: qt6-qtwebengine
Requires: %{_lib}Qt6WebEngineCore
Requires: typelib(AppIndicator3)

# Wrong but for now lets add it as workaround
Requires: python-qt6-devel

%description
RGB lighting management front-end application for OpenRazer with a
graphical, command line and tray applet interface.

%prep
%autosetup -n polychromatic-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang polychromatic

%files -f polychromatic.lang
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/autostart/polychromatic-autostart.desktop
%{_bindir}/polychromatic-*
%{_datadir}/applications/polychromatic.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/polychromatic/
%{_datadir}/metainfo/
%{python_sitelib}/polychromatic/
%{_mandir}/man1/polychromatic-*
