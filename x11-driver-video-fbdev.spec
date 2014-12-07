Summary:	X.org driver for Linux FBDev
Name:		x11-driver-video-fbdev
Version:	0.4.4
Release:	11
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
%setup -qn xf86-video-fbdev-%{version}
%patch1 -p1
autoreconf -vif

%build
%configure	--enable-pciaccess
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.*

