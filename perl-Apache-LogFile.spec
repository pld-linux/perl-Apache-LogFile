%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	LogFile
Summary:	Apache::LogFile - Interface to Apache's logging routines
Summary(pl):	Apache::LogFile - Interfejs do procedur loguj±cych Apache
Name:		perl-Apache-LogFile
Version:	0.12
Release:	2
License:	Apache Group
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	apache-mod_perl
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
Requires:	apache-mod_perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PerlLogFile directive can be used to hook a Perl filehandle to a
piped logger or to a file open for appending. If the first character
of the filename is a |, the file handle is opened as a pipe to the
given program. The file or program can be relative to the ServerRoot.

%description -l pl
Dyrektywa PerlLogFile mo¿e byæ u¿ywa do przekierowania perlowego
uchwytu pliku rurk± do procesu loguj±cego lub do pliku otwartego do
dopisywania. Je¿eli pierwszym znakiem nazwy pliku jest |, uchwyt jest
otwierany jako rurka do podanego programu. ¦cie¿ka do pliku lub
programu mo¿e byæ wzglêdna w stosunku do ServerRoot.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{perl_sitearch}/Apache/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/%{pdir}/*.pm
%{perl_sitearch}/%{pdir}/%{pnam}
%dir %{perl_sitearch}/auto/Apache/LogFile
%attr(755,root,root) %{perl_sitearch}/auto/Apache/LogFile/*.so
%{perl_sitearch}/auto/Apache/LogFile/*.bs
%dir %{perl_sitearch}/auto/Apache/LogFile/Config
%attr(755,root,root) %{perl_sitearch}/auto/Apache/LogFile/Config/*.so
%{perl_sitearch}/auto/Apache/LogFile/Config/*.bs
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
