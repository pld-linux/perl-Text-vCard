#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	vCard
Summary:	perl(Text::vCard) module
Name:		perl-Text-vCard
Version:	1.98
Release:	0.1
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ecefb3c7c6ac62bf5fc56aa35fc6d63
Patch0:		%{name}
# most of CPAN modules have generic URL (substitute pdir and pnam here)
#URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#BuildRequires:	-
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Text-vFile-asData
%endif
#Requires:	-
#Provides:	-
#Obsoletes:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description 
--RAW--
A vCard is an electronic business card.
This package is for a single vCard (person / record / set of address
information).  It provides an API to editing and creating vCards, or supplied a
specific piece of the Text::vFile::asData results it generates a vCard with
that content.  
This package provides an API to reading / editing and creating multiple vCards. A vCard is an electronic business card.  
This package has been developed based on rfc2426.  
You will find that many applications (Apple Address book, MS Outlook, Evolution etc) can export and import vCards.


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
# note it's mostly easier to copy unpackaged filelist here, and run adapter over the spec.
# use macros:
%dir %attr(755,root,root) %{perl_vendorlib}/Text/vCard
%{perl_vendorlib}/Text/vCard.pm
%{perl_vendorlib}/Text/vCard/*.pm
%{_mandir}/man3/*
