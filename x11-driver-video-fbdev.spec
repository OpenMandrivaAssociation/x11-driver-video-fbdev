Name: x11-driver-video-fbdev
Version: 0.4.3
Release: 2
Summary: X.org driver for Linux FBDev
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-fbdev is the X.org driver for Linux FBDev.

%prep
%setup -qn xf86-video-fbdev-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.*



%changelog
* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.3-1
+ Revision: 808300
- version update 0.4.3

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.4.2-8
+ Revision: 787223
- Build for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.4.2-7
+ Revision: 748401
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-6
+ Revision: 703725
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.4.2-5
+ Revision: 683547
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-4
+ Revision: 671145
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.4.2-3mdv2011.0
+ Revision: 595707
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.4.2-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Apr 05 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.4.2-1mdv2010.1
+ Revision: 531583
- New version: 0.4.2

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 0.4.1-2mdv2010.1
+ Revision: 464337
- rebuild for new xserver

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 407717
- fix build
- new release

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 0.4.0-4mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.0-3mdv2009.1
+ Revision: 308166
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-2mdv2009.0
+ Revision: 265919
- rebuild early 2009.0 package (before pixel changes)
- improved description
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.4.0-1mdv2009.0
+ Revision: 194208
- Update to version 0.4.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.3.1-4mdv2008.1
+ Revision: 165552
- Revert to use upstream tarball and remove local patches.

  + Ademar de Souza Reis Jr <ademar@mandriva.com.br>
    - re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.3.1-3mdv2008.1
+ Revision: 154860
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Fix tarball to use existing tag xf86-video-fbdev-0.3.1. Also dont move
  back mandriva branch point and update, as a set of patches, changes up to
  there.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.3.1-2mdv2008.1
+ Revision: 98691
- minor spec cleanup
- build against new xserver (1.4)

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

