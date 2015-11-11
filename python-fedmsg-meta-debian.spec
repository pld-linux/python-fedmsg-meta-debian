#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	fedmsg_meta_debian
Summary:	Metadata providers for Debian's fedmsg deployment
Name:		python-fedmsg-meta-debian
Version:	0.1
Release:	0.2
License:	MIT
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	39bd5042627aff42b4f17cb8fa8c10ec
URL:		http://pypi.python.org/pypi/fedmsg_meta_debian
BuildRequires:	fedmsg >= 0.6.1
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	fedmsg >= 0.6.1
#Requires:	python-fedora
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fedmsg <http://fedmsg.com> is a set of tools for knitting together
services and webapps into a realtime messaging net. This package
contains metadata provider plugins for the Debian deployment of that
system.

If you were to deploy fedmsg at another site, you would like want to
write your own module like this one that could provide textual
representations of your messages.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info in case it exists
rm -r %{module}.egg-info

%build
%{__python} setup.py build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/fedmsg_meta_debian
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
