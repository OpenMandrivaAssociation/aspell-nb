%define src_ver 0.50.1-0
%define languageenglazy Norwegian Bokmaal
%define languagecode nb
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.1
Release:	%mkrel 8
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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-5mdv2011.0
+ Revision: 662854
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-4mdv2011.0
+ Revision: 603446
- rebuild

* Mon Mar 15 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.50.1-3mdv2010.1
+ Revision: 520572
- revert ignorant noarch change of mine :/ (fixes #58188)

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.50.1-2mdv2010.1
+ Revision: 518947
- rebuild

* Tue Jun 16 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.50.1-1mdv2010.0
+ Revision: 386308
- * update to new aspell-nb replacing deprecated aspell-no package
  * make package noarch
  * cleanups!
- 'aspell-no' is deprecated package and 'no' is a deprecated language code, rename..

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.50.2-12mdv2009.1
+ Revision: 350083
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-11mdv2009.0
+ Revision: 220435
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.50.2-10mdv2008.1
+ Revision: 182508
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-9mdv2008.1
+ Revision: 148838
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-8mdv2007.0
+ Revision: 123343
- Import aspell-no

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-8mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.2-7mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-6mdk
- allow build on ia64

