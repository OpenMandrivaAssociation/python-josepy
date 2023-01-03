Name:		python-josepy
Version:	1.13.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/j/josepy/josepy-%{version}.tar.gz
Summary:	JOSE protocol implementation in Python
URL:		https://pypi.org/project/josepy/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
JOSE protocol implementation in Python

%prep
%autosetup -p1 -n josepy-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/jws
%{py_sitedir}/josepy
%{py_sitedir}/josepy-*.*-info
