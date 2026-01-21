Name:		python-josepy
Version:	2.2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/j/josepy/josepy-%{version}.tar.gz
Summary:	JOSE protocol implementation in Python
URL:		https://pypi.org/project/josepy/
License:	Apache License 2.0
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildArch:	noarch

%description
JOSE protocol implementation in Python

%files
%{_bindir}/jws
%{py_sitedir}/josepy
%{py_sitedir}/josepy-*.*-info
