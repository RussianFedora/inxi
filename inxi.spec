%global svnrev  2033

aa

Name:           inxi
Version:        1.9.12
Release:        5%{?dist}
Summary:        A full featured system information script
Summary(ru):    Скрипт вывода полной информации об оборудовании и системе

License:        GPLv3
URL:            http://code.google.com/p/inxi/
Source0:        http://inxi.googlecode.com/svn-history/r%{svnrev}/trunk/%{name}.tar.gz

BuildArch:      noarch

Requires:       net-tools
Requires:       pciutils
Requires:       procps
Requires:       lm_sensors
Requires:       usbutils
Requires:       hddtemp
Requires:       xorg-x11-utils

%description
Inxi offers a wide range of built-in options, as well as a good number of extra
features which require having the script recommends installed on the system.


%description -l ru
Inxi позволяет выводить различную информацию об используемом оборудовании и о
работе системы.


%prep
%setup -q -c
chmod -x %{name}.changelog


%build


%install
install -p -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -p -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%files
%doc %{name}.changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Aug 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-5
- Correct executable permissions

* Wed Aug 07 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-4
- Removed unnecessary Requires

* Tue Aug 06 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-3
- Change source0 link
- Added Requires

* Tue Aug 06 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-2
- Correct spec and descriptions

* Wed Jul 03 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-1
- Update to 1.9.12

* Tue Jun 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.9-1
- Update to 1.9.9

* Tue Jun 04 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.7-1
- Update to 1.9.7

* Tue May 07 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.47-1
- Update to 1.8.47

* Mon Apr 22 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.45-1
- Initial release
