Name:           ocaml-rtime
Version:        0.9.1
Release:        2
Summary:        OCaml module implementing timelines for ocaml-react
License:        new BSD
Group:          Development/Other
URL:            http://erratique.ch/software/rtime
Source0:        http://erratique.ch/software/rtime/releases/rtime-%{version}.tbz
BuildRequires:  ocaml
BuildRequires:  ocaml-react-devel

%description
Rtime is an OCaml module implementing timelines for React. It manages
time stamp events, delayed events and delayed signals along timelines.
A timeline is defined by an absolute notion of time provided by the client.
Running the timeline at the appropriate pace is left to the client.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n rtime-%{version}

%build
chmod u+x build
./build module-byte
./build module-native
#./build module-plugin

%install
INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/rtime ./build install
INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/rtime ./build install-byte
#INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/rtime ./build install-plugin

# "The tests may fail in a heavily loaded environment" which the BS is
#%check
#INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/rtime ./build test.native
#./test.native -p 0.02

%files
%defattr(-,root,root)
%doc README CHANGES
%dir %{_libdir}/ocaml/rtime
%{_libdir}/ocaml/rtime/META
%{_libdir}/ocaml/rtime/rtime.cmi
%{_libdir}/ocaml/rtime/rtime.cmo

%files devel
%defattr(-,root,root)
%doc doc test
%{_libdir}/ocaml/rtime/rtime.ml
%{_libdir}/ocaml/rtime/rtime.mli 
%{_libdir}/ocaml/rtime/rtime.cmx
%{_libdir}/ocaml/rtime/rtime.o
#%{_libdir}/ocaml/rtime/rtime.cmxs



%changelog
* Thu Apr 22 2010 Florent Monnier <blue_prawn@mandriva.org> 0.9.1-1mdv2010.1
+ Revision: 538010
- updated to version 0.9.1

* Thu Aug 13 2009 Florent Monnier <blue_prawn@mandriva.org> 0.9.0-2mdv2010.0
+ Revision: 415833
- the tests may fail in a heavily loaded environment
- precision set
- import ocaml-rtime

