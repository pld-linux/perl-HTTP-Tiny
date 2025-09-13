#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	HTTP
%define		pnam	Tiny
Summary:	HTTP::Tiny - A small, simple, correct HTTP/1.1 client
Summary(pl.UTF-8):	HTTP::Tiny - mały, prosty, poprawny klient HTTP/1.1
Name:		perl-HTTP-Tiny
Version:	0.090
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9fa1ba04f168c57f5aca78ab3e1f8fb2
URL:		https://metacpan.org/dist/HTTP-Tiny
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple HTTP/1.1 client, designed for doing simple
requests without the overhead of a large framework like
LWP::UserAgent.

It is more correct and more complete than HTTP::Lite. It supports
proxies and redirection. It also correctly resumes after EINTR.

If IO::Socket::IP 0.25 or later is installed, HTTP::Tiny will use it
instead of IO::Socket::INET for transparent support for both IPv4 and
IPv6.

Cookie support requires HTTP::CookieJar or an equivalent class.

%description -l pl.UTF-8
Ten moduł to bardzo prosty klient HTTP/1.1, zaprojektowany do
wykonywania prostych żądań bez narzutu całego szkieletu, takiego jak
LWP::UserAgent.

Jest bardziej poprawny i kompletni niż HTTP::Lite. Obsługuje proxy i
przekierowania. Poprawnie też wznawia po EINTR.

Jeśli zainstalowany jest IO::Socket::IP w wersji 0.25 lub nowszej,
HTTP::Tiny używa go zamiast IO::Socket::INET w celu przezroczystej
obsługi zarówno IPv4, jak i IPv6.

Obsługa ciasteczek wymaga HTTP::CookieJar lub równoważnej klasy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTTP/Tiny.pm
%{_mandir}/man3/HTTP::Tiny.3pm*
%{_examplesdir}/%{name}-%{version}
