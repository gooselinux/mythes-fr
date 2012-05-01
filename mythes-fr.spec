Name: mythes-fr
Summary: French thesaurus
Version: 2.1
Release: 5.1%{?dist}
Source: http://download.tuxfamily.org/dicollecte2/thesaurus_2-1.zip
Group: Applications/Text
URL: http://dicollecte.tuxfamily.org/home.php?prj=fr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

%description
French thesaurus.

%prep
%setup -q -c

%build
for i in README_th_fr_FR_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_fr_FR_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_fr_FR_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.1-5.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Caolan McNamara <caolanm@redhat.com> - 2.1-4
- tidy spec

* Sat May 23 2009 Caolan McNamara <caolanm@redhat.com> - 2.1-3
- update to new location

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Caolan McNamara <caolanm@redhat.com> - 2.1-1
- initial version
