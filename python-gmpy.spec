%define module	gmpy
%define name	python-%{module}
%define version 1.11
%define release %mkrel 1

Summary:	Python interface to GMP
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.zip
License: 	LGPLv2.1
Group: 		Development/Python
Url: 		http://code.google.com/p/gmpy/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
# GMP versions before 4.2.4 have a bug that cause gmpy to segfault.
Requires:	libgmp >= 4.2.4
BuildRequires:	libgmp-devel >= 4.2.4
%py_requires -d

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
%__rm -rf %{buildroot}
%__python ./setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README lgpl-2.1.txt doc/ test/
