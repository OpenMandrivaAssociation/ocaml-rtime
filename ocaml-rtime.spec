%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml module implementing timelines for ocaml-react
Name:		ocaml-rtime
Version:	0.9.3
Release:	2
License:	BSD
Group:		Development/Other
Url:		http://erratique.ch/software/rtime
Source0:	http://erratique.ch/software/rtime/releases/rtime-%{version}.tbz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-react-devel
Requires:	ocaml-react

%description
Rtime is an OCaml module implementing timelines for React. It manages
time stamp events, delayed events and delayed signals along timelines.
A timeline is defined by an absolute notion of time provided by the client.
Running the timeline at the appropriate pace is left to the client.

%files
%doc README CHANGES
%dir %{_libdir}/ocaml/rtime
%{_libdir}/ocaml/rtime/META
%{_libdir}/ocaml/rtime/rtime.cmi
%{_libdir}/ocaml/rtime/rtime.cma
%{_libdir}/ocaml/rtime/rtime.cmxs

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Requires:	ocaml-react-devel

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc doc/ test/
%{_libdir}/ocaml/rtime/rtime.mli 
%{_libdir}/ocaml/rtime/rtime.cmxa
%{_libdir}/ocaml/rtime/rtime.cmx
%{_libdir}/ocaml/rtime/rtime.a

#----------------------------------------------------------------------------

%prep
%setup -q -n rtime-%{version}

%build
ocaml setup.ml -configure
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install \
	--prefix %{_prefix} \
	--libdir %{_libdir} \
	--libexecdir %{_libexecdir} \
	--exec-prefix %{_exec_prefix} \
	--bindir %{_bindir} \
	--mandir %{_mandir} \
	--datadir %{_datadir} \
	--destdir %{buildroot}

