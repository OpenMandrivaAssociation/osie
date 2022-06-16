Name:		osie
Version:	1.0.0
Release:	3
Summary:	OpenTTD screenshot information extractor
Group:          Graphics
License:	GPLv2
Url:		http://www.openttd.org/
Source0:	http://ftp.snt.utwente.nl/pub/games/openttd/binaries/extra/%{name}/%{version}/%{name}-%{version}-source.tar.gz
BuildRequires:	png-devel

%description
osie (OpenTTD screenshot information extractor) extracts the information
stored in OpenTTD's PNG screenshots such as the version, NewGRFs and AIs.

%prep
%autosetup -p1

cat >> Makefile.local << EOF
prefix = %{_prefix}
DO_NOT_INSTALL_CHANGELOG = 1
DO_NOT_INSTALL_LICENSE = 1
DO_NOT_INSTALL_DOCS = 1
EOF

%build
%setup_compile_flags
%make_build VERBOSE=1

%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root)
%doc docs/readme.txt changelog.txt
#{_bindir}/%{name}
#{_mandir}/man1/%{name}.1.*


%changelog
* Wed Jan 26 2011 Jani Välimaa <wally@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 632924
- imported package osie

