%define		module	gbinder
Summary:	-
Summary(pl.UTF-8):	-
# Name must match the python module/package name (as on pypi or in 'import' statement)
Name:		python3-%{module}
Version:	1.1.1
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Libraries/Python
Source0:	https://github.com/erfanoabdi/gbinder-python/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	47e15c2768963a5184a489ae2d073116
URL:		https://github.com/erfanoabdi/gbinder-python
BuildRequires:	libgbinder-devel
BuildRequires:	libglibutil-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{module}-python-%{version}

# fix #!/usr/bin/env python -> #!/usr/bin/python:
#%{__sed} -i -e '1s,^#!.*python3,#!%{__python3},' %{name}.py

%build
%py3_build build_ext --cython

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{py3_sitedir}/%{module}.*.so
%{py3_sitedir}/gbinder_python-%{version}-py*.egg-info
