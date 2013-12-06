%define src_ver 0.50.1-0
%define languageenglazy Norwegian Bokmaal
%define languagecode nb
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.1
Release:	10
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.sourceforge.net/
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

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

%files
%doc README Copyright
%{_libdir}/aspell-*/*

