Name		: firefox
Version		: 1.0.7
Release		: 1%{?dist}
# If %{dist} is defined, insert its value here. If not, do nothing.
# See http://fedoraproject.org/wiki/DistTag

License		: MPL
Summary		: Mozilla Firefox Web browser.
Group		: Applications/Internet

URL		: http://www.mozilla.org/products/firefox/
Vendor		: Mozilla Foundation
Packager	: Thomas Chung <tchung@fedoranews.org>

BuildRoot	: %{_tmppath}/%{name}-%{version}-buildroot
Source0		: %{name}-%{version}.tar.gz
Source1		: firefox.desktop
Source2		: firefox.png

AutoReq     	: No
AutoProv	: No

Requires        : libstdc++.so.5

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%prep
rm -rf %{buildroot}

#######################################################################
# setup macro
# -a num  : Only unpack source number after changing to the directory
# -b num  : Only unpack source number before changing to the directory
# -c      : Create directory before unpacking.
# -D      : Do not delete the directory before unpacking
# -n name : Name the directory as name
# -q      : Run quiety with minimum output
# -T      : Disable the automatic unpacking of the archives.
#######################################################################
%setup -c -q

#########################################################
# Common Red Hat RPM macros (rpm --showrc for more info)
# {_sourcedir} : /usr/src/redhat/SOURCES
# {_builddir}  : /usr/src/redhat/BUILD
# {_tmppath}   : /var/tmp
# {_libdir}    : /usr/lib
# {_bindir}    : /usr/bin
# {_datadir}   : /usr/share
# {_mandir}    : /usr/share/man
# {_docdir}    : /usr/share/doc
# {buildroot}
# {name}
# {version}
# {release}
#########################################################

%install
%{__install} -d -m 755 %{buildroot}%{_libdir}
cp -a firefox %{buildroot}%{_libdir}
%{__install} -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/firefox.desktop
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/firefox.png
%{__install} -d -m 755 %{buildroot}%{_bindir}
ln -s %{_libdir}/firefox/firefox %{buildroot}%{_bindir}/firefox
ln -s %{_libdir}/firefox/firefox-bin %{buildroot}%{_bindir}/firefox-bin

%post
rm -rf %{_libdir}/firefox/plugins
ln -sf %{_libdir}/mozilla/plugins %{_libdir}/firefox/plugins

%clean
rm -rf %{buildroot}

%files 
#####################################################
# defattr sets the default attributes for all files
#####################################################
%defattr(-, root, root)
%{_libdir}/firefox/*
%{_datadir}/applications/firefox.desktop
%{_datadir}/pixmaps/firefox.png
%{_bindir}/firefox
%{_bindir}/firefox-bin

%changelog
* Tue Sep 20 2005 Thomas Chung <tchung@fedoranews.org> 1.0.7-1
- Version 1.0.7

* Tue Jul 19 2005 Thomas Chung <tchung@fedoranews.org> 1.0.6-1
- Version 1.0.6

* Tue Jul 12 2005 Thomas Chung <tchung@fedoranews.org> 1.0.5-1
- Version 1.0.5
- Use {?dist} tag
- Requires libstdc++.so.5

* Thu May 12 2005 Thomas Chung <tchung@fedoranews.org> 1.0.4-0
- Version 1.0.4
- Remove firefox plugins and link to mozilla plugins

* Mon Apr 18 2005 Thomas Chung <tchung@fedoranews.org> 1.0.3-0
- Version 1.0.3

* Wed Mar 23 2005 Thomas Chung <tchung@fedoranews.org> 1.0.2-0
- Version 1.0.2

* Thu Feb 24 2005 Thomas Chung <tchung@fedoranews.org> 1.0.1-0
- Version 1.0.1
- Disable Epoch

* Tue Nov 09 2004 Thomas Chung <tchung@fedoranews.org> 2:1.0
- Version 1.0 Final
- Increased Epoch number to handle upgrading lower version

* Thu Nov 04 2004 Thomas Chung <tchung@fedoranews.org> 1:1.0rc2
- Rebuild for 1.0 Release Candidate 2

* Wed Oct 27 2004 Thomas Chung <tchung@fedoranews.org> 1:1.0rc1
- Rebuild for 1.0 Release Candidate 1

* Fri Oct 08 2004 Thomas Chung <tchung@fedoranews.org> 1:0.10.1
- Rebuild for 1.0 Preview Release Update 1
- Renumber version to 0.10.1
- Use Epoch to handle upgrading lower version
- Use %{__install} tag

* Tue Sep 14 2004 Thomas Chung <tchung@fedoranews.org> 1.0PR
- Rebuild for 1.0 Preview Release

* Fri Aug 06 2004 Thomas Chung <tchung@fedoranews.org> 0.9.3
- Initial RPM Build
