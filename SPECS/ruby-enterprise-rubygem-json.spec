%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from json-1.4.6.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname json
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%define __arch_install_post   /usr/lib/rpm/check-rpaths

Summary: JSON Implementation for Ruby
Name: ruby-enterprise-rubygem-%{gemname}
Version: 1.4.6
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://flori.github.com/json
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise-rubygems
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
This is a JSON implementation as a Ruby extension in C.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/edit_json.rb
%{_bindir}/prettify_json.rb
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 1.4.6-2.hhg
- Rebuild for Ruby Enterprise Edition

* Thu May 05 2011 Sergio Rubio <rubiojr@frameos.org> - 1.4.6-2
- buildrequire ruby-devel

* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 1.4.6-1
- Initial package
