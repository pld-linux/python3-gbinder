%define		module	gbinder
Summary:	Cython extension module for C++ gbinder functions
Summary(pl.UTF-8):	Moduł rozszerzenia Cythona do funkcji C++ biblioteki gbinder
Name:		python3-%{module}
Version:	1.2.1
Release:	1
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/gbinder/
Source0:	https://files.pythonhosted.org/packages/source/g/gbinder/%{module}-%{version}.tar.gz
# Source0-md5:	5e7576075821dd2ca3b153002528ffb8
URL:		https://github.com/Kyle6012/gbinder
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
Cython extension module for C++ gbinder functions.

%description -l pl.UTF-8
Moduł rozszerzenia Cythona do funkcji C++ biblioteki gbinder.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{py3_sitedir}/gbinder.cpython-*.so
%{py3_sitedir}/gbinder-%{version}-py*.egg-info
