%define module	gmpy
%define name	python-%{module}
%define version 1.01

Summary:	Python interface to GMP
Name:		%{name}
Version:	%{version}
Release:	%mkrel 3
Source0:	%{module}-%{version}.tar.bz2
License: 	GPL
Group: 		Development/Python
Url: 		http://gmpy.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	libgmp
BuildRequires:	libgmp-devel
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
%setup -q -n %{module}

%build
%__python ./setup.py build

%install
rm -rf %{buildroot}
%__python ./setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README doc/ test/



