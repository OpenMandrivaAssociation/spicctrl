%define name spicctrl
%define version 1.9

Summary: Sony Vaio SPIC Control Program
Name: %name
Version: %version
Release: 7
License: GPL
Group: System/Configuration/Hardware
BuildRoot: %{_builddir}/%{name}-buildroot
Source: http://popies.net/sonypi/%name-%version.tar.bz2
URL: http://popies.net/sonypi/

%description
This utility allows one to query and set a variety of parameters on your
Sony Vaio laptop computer, including:

 * AC Power status
 * Battery status 
 * Screen brightness
 * Bluetooth device power status

%prep
%setup 

%build
%make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_sbindir/
install %{_builddir}/%{name}-%{version}/spicctrl $RPM_BUILD_ROOT/usr/sbin

%post
if [ ! -c /dev/sonypi ]; then
	rm -f /dev/sonypi
	mknod /dev/sonypi c 10 250
fi
grep 'alias char-major-10-250 sonypi' /etc/modules.conf > /dev/null
RETVAL=$?
if [ $RETVAL -ne 0 ]; then
	echo 'alias char-major-10-250 sonypi' >> /etc/modules.conf
	echo 'options sonypi minor=250' >> /etc/modules.conf
	echo 'alias char-major-10-250 sonypi' >> /etc/modprobe.conf
	echo 'options sonypi minor=250' >> /etc/modprobe.conf
fi

%files
%defattr(-,root,root)
%_sbindir/*
%doc AUTHORS LICENSE CHANGES




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.9-6mdv2010.0
+ Revision: 434054
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.9-5mdv2009.0
+ Revision: 260948
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.9-4mdv2009.0
+ Revision: 252944
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.9-2mdv2008.1
+ Revision: 140850
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Feb 24 2007 Giuseppe GhibÃ² <ghibo@mandriva.com> 1.9-2mdv2007.0
+ Revision: 125409
- Rebuilt.
- Import spicctrl

* Sat Aug 06 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1.9-1mdk
- Release: 1.9.

* Mon Mar 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.6.1-1mdk
- from Nicolas Brouard <brouard@ined.fr> :  
	- New release (see sonypid sonypidd new complementary packages)

