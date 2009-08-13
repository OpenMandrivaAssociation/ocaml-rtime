Name:           ocaml-rtime
Version:        0.9.0
Release:        %mkrel 2
Summary:        OCaml module implementing timelines for ocaml-react
License:        new BSD
Group:          Development/Other
URL:            http://erratique.ch/software/rtime
Source0:        http://erratique.ch/software/rtime/releases/rtime-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
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
./build module-byte
./build module-native
#./build module-plugin

%install
rm -rf %{buildroot}
INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/rtime ./build install
INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/rtime ./build install-byte
#INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/rtime ./build install-plugin

# "The tests may fail in a heavily loaded environment" which the BS is
#%check
#INSTALLDIR=%{buildroot}/%{_libdir}/ocaml/rtime ./build test.native
#./test.native -p 0.02

%clean
rm -rf %{buildroot}

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

