Summary:	X.org driver for Linux FBDev
Name:		x11-driver-video-fbdev
Version:	0.5.0
Release:	5
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-%{version}.tar.bz2
Patch1:		BGNoneRoot.patch

BuildRequires:	pkgconfig(pciaccess)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-fbdev is the X.org driver for Linux FBDev.

%prep
%autosetup -n xf86-video-fbdev-%{version} -p1
autoreconf -vif
sed 's/if XV/ifdef XV/' -i src/fbdev.c

%build
%configure \
	--enable-pciaccess

%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.*

