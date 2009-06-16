%define src_ver 0.50.1-0
%define languageenglazy Norwegian Bokmaal
%define languagecode nb

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.1
Release:	%mkrel 1
Group:		System/Internationalization
Source0:	ftp://ftp.gnu.org/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides:	spell-no
Provides:	spell-nb

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50

# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-no = 0.50.2-13
Obsoletes:	aspell-no

BuildArch:	noarch

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright
%{_libdir}/aspell-*/*
