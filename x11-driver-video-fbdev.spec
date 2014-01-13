Summary:	X.org driver for Linux FBDev
Name:		x11-driver-video-fbdev
Version:	0.4.3
Release:	6
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-%{version}.tar.bz2
Patch0:		0001-Remove-mibstore.h.patch
Patch1:		BGNoneRoot.patch

BuildRequires:	pkgconfig(pciaccess)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-fbdev is the X.org driver for Linux FBDev.

%prep
%setup -qn xf86-video-fbdev-%{version}
%patch0 -p1
%patch1 -p1
autoreconf -vif

%build
%configure2_5x	--enable-pciaccess
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.*

