Name:		x11-driver-video-fbdev
Version:	0.4.3
Release:	4
Summary:	X.org driver for Linux FBDev
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-%{version}.tar.bz2
Patch0:		0001-Remove-mibstore.h.patch
Patch1:		BGNoneRoot.patch

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.13
BuildRequires:	x11-util-macros >= 1.0.1

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts:	xorg-x11-server < 7.0

%description
x11-driver-video-fbdev is the X.org driver for Linux FBDev.

%prep
%setup -qn xf86-video-fbdev-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.*
