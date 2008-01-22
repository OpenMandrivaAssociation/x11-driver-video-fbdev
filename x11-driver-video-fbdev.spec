Name: x11-driver-video-fbdev
Version: 0.3.1
Release: %mkrel 4
Summary: The X.org driver for Linux FBDev
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-fbdev  xorg/drivers/xf86-video-fbdev
# cd xorg/drivers/xf86-video/fbdev
# git-archive --format=tar --prefix=xf86-video-fbdev-0.3.1/ xf86-video-fbdev-0.3.1 | bzip2 -9 > xf86-video-fbdev-0.3.1.tar.bz2
########################################################################
Source0: xf86-video-fbdev-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-fbdev-0.3.1..origin/mandriva+gpl
Patch1: 0001-Only-determine-pitch-after-setting-initial-mode.patch
Patch2: 0002-Add-conditional-support-for-pci-rework-branch.patch
Patch3: 0003-Replace-a-non-ascii-char-with-the-corresponding-grof.patch
Patch4: 0004-Fixed-leftover-PCIACCESS-XSERVER_LIBPCIACCESS.patch
Patch5: 0005-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Linux FBDev

%prep
%setup -q -n xf86-video-fbdev-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.*
