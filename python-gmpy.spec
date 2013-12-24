%define module	gmpy

Summary:	Python interface to GMP
Name:		python-%{module}
Version:	1.17
Release:	2
Source0:	http://gmpy.googlecode.com/files/gmpy-%{version}.zip
License: 	LGPLv2.1
Group: 		Development/Python
Url: 		http://code.google.com/p/gmpy/
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
