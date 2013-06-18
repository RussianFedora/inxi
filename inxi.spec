Name:           inxi
Version:        1.9.9
Release:        1%{?dist}
Summary:        A full featured system information script

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
Iinxi: A full featured system information script

Inxi offers a wide range of built-in options, as well as a good number of extra
features which require having the script recommends installed on the system.
Check recommends to see what's needed for each extra feature. Check sources for
latest inxi version number.

%prep
%setup -q


%build


%install
install -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%files
%doc %{name}.changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jun 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.9-1
- Update to 1.9.9

* Tue Jun 04 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.7-1.R
- Update to 1.9.7

* Tue May 07 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.47-1.R
- Update to 1.8.47

* Mon Apr 22 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.45-1.R
- Initial release
