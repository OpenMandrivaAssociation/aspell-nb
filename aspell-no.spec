%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-2
%define languagelocal norsk
%define languageeng norwegian
%define languageenglazy Norwegian
%define languagecode no

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.2
Release:       %mkrel 12
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.sourceforge.net/
License:       GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-no

BuildRequires: aspell >= 0.50
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary

Autoreqprov:   no

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

chmod 644 README Copyright

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Copyright
%{_libdir}/aspell-*/*


