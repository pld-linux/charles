# I have no access to full version, so I'm packaging trial version only.
# If you have full tarball, add with(out?)_trial bcond

# Conditional build:
%bcond_without	trial		# build from full tarball

%define		rel	0.1
%include	/usr/lib/rpm/macros.java
Summary:	Web debugging proxy application
Name:		charles
Version:	3.4.1
Release:	%{_rel}
License:	Proprietary, not distributable
Group:		Networking/Daemons
Source0:	http://www.charlesproxy.com/assets/release/%{version}/charles.tar.gz
# NoSource0-md5:	bcab2cd381d8f5ae9ffed08a0a89b76d
NoSource:	0
Source1:	%{name}.sh
URL:		http://www.charlesproxy.com/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre-X11
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# already stripped
%define		_enable_debug_packages	0

%description
Charles is an HTTP proxy / HTTP monitor / Reverse Proxy that enables a
developer to view all of the HTTP and SSL / HTTPS traffic between
their machine and the Internet. This includes requests, responses and
the HTTP headers (which contain the cookies and caching information).

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir}/%{name},%{_libdir}/%{name},%{_bindir}}

cp -a lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
%ifarch %{ix86}
install -p lib/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}
%endif
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}
%ifarch %{ix86}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libjdic.so
%endif
