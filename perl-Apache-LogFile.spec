%define		pdir	Apache
%define		pnam	LogFile
Summary:	Apache::LogFile - interface to Apache's logging routines
Summary(pl.UTF-8):	Apache::LogFile - interfejs do procedur logujących Apache'a
Name:		perl-Apache-LogFile
Version:	0.12
Release:	6
License:	Apache Group
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	11d254d35003131fd1051ba14ee3107a
URL:		http://search.cpan.org/dist/Apache-LogFile/
BuildRequires:	apache1-devel
BuildRequires:	apache1-mod_perl
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-26
Requires:	apache1-mod_perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PerlLogFile directive can be used to hook a Perl filehandle to a
piped logger or to a file open for appending. If the first character
of the filename is a |, the file handle is opened as a pipe to the
given program. The file or program can be relative to the ServerRoot.

%description -l pl.UTF-8
Dyrektywa PerlLogFile może być używa do przekierowania perlowego
uchwytu pliku rurką do procesu logującego lub do pliku otwartego do
dopisywania. Jeżeli pierwszym znakiem nazwy pliku jest |, uchwyt jest
otwierany jako rurka do podanego programu. Ścieżka do pliku lub
programu może być względna w stosunku do ServerRoot.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{perl_sitearch}/Apache/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/%{pdir}/%{pnam}
%dir %{perl_vendorarch}/auto/Apache/LogFile
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/LogFile/*.so
%dir %{perl_vendorarch}/auto/Apache/LogFile/Config
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/LogFile/Config/*.so
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
