Summary: Split a multi-routine Fortran file into individual files
Name: fsplit
Version: 5.5
Release: %mkrel 6
License: BSD
Group: Development/Other
Source0: fsplit.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Fsplit takes as input either a file or standard input containing Fortran source
code.  It attempts to split the input into separate routine files of the form
name.f, where name is the name of the program unit (e.g.  function, subroutine,
block data or program).

%prep
%setup -q -n %{name}

%build
%make CFLAGS="%optflags" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 -s fsplit $RPM_BUILD_ROOT/%{_bindir}
install -m 644 fsplit.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/fsplit
%{_mandir}/man1/fsplit.1*


