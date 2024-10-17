%define debug_package %{nil}

Summary: Sony Vaio SPIC Control Program
Name: spicctrl
Version: 1.9
Release: 1
License: GPL
Group: System/Configuration/Hardware
BuildRoot: %{_builddir}/%{name}-buildroot
Source: http://popies.net/sonypi/spicctrl-%{version}.tar.bz2
URL: https://popies.net/sonypi/
ExclusiveArch: %{ix86} %{x86_64}

%description
This utility allows one to query and set a variety of parameters on your
Sony Vaio laptop computer, including:

 * AC Power status
 * Battery status 
 * Screen brightness
 * Bluetooth device power status

%prep
%autosetup -p1

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%_bindir/
install %{_builddir}/%{name}-%{version}/spicctrl $RPM_BUILD_ROOT%_bindir/

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
%_bindir/*
%doc AUTHORS LICENSE CHANGES
