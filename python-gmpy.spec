%define module	gmpy

Summary:	Python interface to GMP
Name:		python-%{module}
Version:	1.16
Release:	1
Source0:	%{module}-%{version}.zip
License: 	LGPLv2.1
Group: 		Development/Python
Url: 		http://code.google.com/p/gmpy/
Requires:	gmp
BuildRequires:	gmp-devel >= 4.2.4
BuildRequires:  python-devel

%description
The General Multiprecision PYthon project (GMPY) focuses on
Python-usable modules providing multiprecision arithmetic
functionality to Python programmers. The project mission includes both
C and C++ Python-modules (for speed) and pure Python modules (for
flexibility and convenience); it potentially includes integral,
rational and floating-point arithmetic in any base. Only
cross-platform functionality is of interest, at least for now.

%prep
%setup -q -n %{module}-%{version}

%build
find -name .svn | xargs rm -rf
%__python ./setup.py build

%install
%__python ./setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST
%doc README lgpl-2.1.txt doc/ test/


%changelog
* Tue Jan 17 2012 Lev Givon <lev@mandriva.org> 1.15-1mdv2012.0
+ Revision: 762051
- Update to 1.15.

* Mon Dec 13 2010 Lev Givon <lev@mandriva.org> 1.14-1mdv2011.0
+ Revision: 620654
- Update to 1.14.

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1.12-2mdv2011.0
+ Revision: 594037
- rebuld for py 2.7

* Mon Jul 19 2010 Lev Givon <lev@mandriva.org> 1.12-1mdv2011.0
+ Revision: 554995
- Update to 1.12.

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 1.11-1mdv2010.1
+ Revision: 503561
- New version 1.11
- rebuild for new gmp

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 1.10-1mdv2010.1
+ Revision: 482849
- Update to new version 1.10

* Wed Apr 01 2009 Lev Givon <lev@mandriva.org> 1.04-1mdv2010.0
+ Revision: 363390
- Update to 1.04.

* Fri Jul 11 2008 Lev Givon <lev@mandriva.org> 1.03-1mdv2009.0
+ Revision: 233834
- Update to 1.03.

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.01-3mdv2008.1
+ Revision: 136448
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 21 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.01-3mdv2007.0
+ Revision: 111518
- Rebuicl for new python
- import python-gmpy-1.01-2mdk

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.01-2mdk
- Add BuildRequires
- Fix mkrel for rpmbuildupdate

* Wed May 03 2006 Lev Givon <lev@columbia.edu> 1.01-1mdk
- Initial Mandriva package.

