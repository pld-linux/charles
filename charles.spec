
%include	/usr/lib/rpm/macros.java

%define		_rel	0.1

# I have no access to full version, so I'm packaging trial version only.
# If you have full tarball, add with(out?)_trial bcond
%define		with_trial 1

Summary:	Web debugging proxy application
Name:		charles
Version:	3.4.1
Release:	%{_rel}%{?with_trial:trial}
License:	Proprietary, not distributable
Group:		Development/Languages/Java
Source0:	%{name}.tar.gz
# Source0-md5:	bcab2cd381d8f5ae9ffed08a0a89b76d
NoSource:	0
Source1:	%{name}.sh
URL:		http://www.charlesproxy.com/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre-X11
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

cp -a lib/*jar $RPM_BUILD_ROOT%{_javadir}/%{name}
cp -a lib/*so $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -a %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/%{name}
%{_libdir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}
