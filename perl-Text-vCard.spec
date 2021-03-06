#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Text
%define		pnam	vCard
Summary:	Text::vCard - module to edit and create a single vCard (RFC 2426)
Summary(pl.UTF-8):	Text::vCard - moduł do edycji i tworzenia pojedynczych vCardów (RFC 2426)
Name:		perl-Text-vCard
Version:	3.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d23c610e2159b7d4034275f2bfe27704
URL:		http://search.cpan.org/dist/Text-vCard/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-Directory-Scratch
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Moo
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Most
BuildRequires:	perl-Text-vFile-asData
BuildRequires:	perl-Unicode-LineBreak
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This Perl module implements interface for both single vcard
(Text::vCard) and addressbook (Text::vCard::Addressbook). vCard is an
electronic business card. You will find that many applications (Apple
Address Book, MS Outlook, Evolution etc) can export and import vCards.
This package has been developed based on RFC 2426.  

%description -l pl.UTF-8
Ten moduł Perla implementuje interfejs do pojedynczych vcardów
(Text::vCard) oraz książek adresowych (Text::vCard::Addressbook).
vCard to elektroniczna wizytówka. Jest wiele aplikacji (Apple Address
Book, MS Outlook, Evolution itp.) potrafiących eksportować i
importować vCardy. Ten pakiet został stworzony w oparciu o RFC 2426.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/vCard.pm
%{perl_vendorlib}/vCard
%{perl_vendorlib}/Text/vCard.pm
%{perl_vendorlib}/Text/vCard
%{_mandir}/man3/*
