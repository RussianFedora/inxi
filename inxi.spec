Name:           inxi
Version:        1.9.12
Release:        2%{?dist}
Summary:        A full featured system information script
Summary(ru):    Скрипт вывода полной информации об оборудовании и системе

License:        GPLv3
URL:            http://code.google.com/p/inxi/
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

Requires:       bash
Requires:       coreutils
Requires:       gawk grep
Requires:       net-tools
Requires:       pciutils
Requires:       procps
Requires:       lm_sensors

%description
Inxi offers a wide range of built-in options, as well as a good number of extra
features which require having the script recommends installed on the system.


%description -l ru
Inxi позволяет выводить различную информацию об используемом оборудовании и о
работе системы.


%prep
%setup -q


%build


%install
install -p -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -p -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%files
%doc %{name}.changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
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
