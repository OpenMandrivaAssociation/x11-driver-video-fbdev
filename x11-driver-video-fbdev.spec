%define _disable_ld_no_undefined 1

Summary:	X.org driver for Linux FBDev
Name:		x11-driver-video-fbdev
Version:	0.5.1.1
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
# Replace depreacated freedesktop version with maintainded Xlibre
Source0:	https://github.com/X11Libre/xf86-video-fbdev/archive/xlibre-xf86-video-fbdev-%{version}.tar.gz
#Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-%{version}.tar.xz
Patch1:		BGNoneRoot.patch

BuildRequires:	pkgconfig(pciaccess)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-fbdev is the X.org driver for Linux FBDev.

%prep
%autosetup -n xf86-video-fbdev-xlibre-xf86-video-fbdev-%{version} -p1
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
