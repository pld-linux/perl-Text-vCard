#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	vCard
Summary:	Text::vCard - module to edit and create a single vCard (RFC 2426)
Summary(pl):	Text::vCard - modu� do edycji i tworzenia pojedynczych vCard�w (RFC 2426)
Name:		perl-Text-vCard
Version:	1.98
Release:	0.2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ecefb3c7c6ac62bf5fc56aa35fc6d63
URL:		http://search.cpan.org/dist/Text-vCard/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Text-vFile-asData
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This Perl module implements interface for both single vcard
(Text::vCard) and addressbook (Text::vCard::Addressbook). vCard is an
electronic business card. You will find that many applications (Apple
Address Book, MS Outlook, Evolution etc) can export and import vCards.
This package has been developed based on RFC 2426.  

%description -l pl
Ten modu� Perla implementuje interfejs do pojedynczych vcard�w
(Text::vCard) oraz ksi��ek adresowych (Text::vCard::Addressbook).
vCard to elektroniczna wizyt�wka. Jest wiele aplikacji (Apple Address
Book, MS Outlook, Evolution itp.) potrafi�cych eksportowa� i
importowa� vCardy. Ten pakiet zosta� stworzony w oparciu o RFC 2426.

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
%doc Changes TODO
%{perl_vendorlib}/Text/vCard.pm
%dir %{perl_vendorlib}/Text/vCard
%{perl_vendorlib}/Text/vCard/*.pm
%{_mandir}/man3/*
