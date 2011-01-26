%define name	osie
%define version	1.0.0
%define	release	1

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Summary:	OpenTTD screenshot information extractor
Group:          Graphics
License:	GPLv2
URl:		http://www.openttd.org/
Source0:	http://ftp.snt.utwente.nl/pub/games/openttd/binaries/extra/%{name}/%{version}/%{name}-%{version}-source.tar.gz
Patch0:		osie-1.0.0-add_makefile.local_support.patch
BuildRequires:	png-devel

%description
osie (OpenTTD screenshot information extractor) extracts the information
stored in OpenTTD's PNG screenshots such as the version, NewGRFs and AIs.

%prep
%setup -q
%patch0 -p0 -b .addlocalsupport

cat >> Makefile.local << EOF
prefix = %{_prefix}
DO_NOT_INSTALL_CHANGELOG = 1
DO_NOT_INSTALL_LICENSE = 1
DO_NOT_INSTALL_DOCS = 1
EOF

%build
%setup_compile_flags
%make VERBOSE=1

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/readme.txt changelog.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
