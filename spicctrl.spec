%define name spicctrl
%define version 1.9

Summary: Sony Vaio SPIC Control Program
Name: %name
Version: %version
Release: %mkrel 4
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


