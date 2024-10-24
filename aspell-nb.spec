%define src_ver 0.50.1-0
%define languageenglazy Norwegian Bokmaal
%define languagecode nb
%define aspellrelease 0.60
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.1_0
Release:	1
Group:		System/Internationalization
License:	GPLv2
Url:		https://aspell.sourceforge.net/
Source0:	ftp://ftp.gnu.org/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-no = 0.50.2-13
Provides:	spell-no
Provides:	spell-nb

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}
%autopatch -p1
cp bokmal.alias bokmål.alias

%build
# don't use configure macro
./configure

%make_build

%install
%make_install
mv %{buildroot}%{_libdir}/aspell-%{aspellrelease}/'bokm'$'\345''l.alias' %{buildroot}%{_libdir}/aspell-%{aspellrelease}/bokmål.alias

%files
%doc README Copyright
%{_libdir}/aspell-*/*

