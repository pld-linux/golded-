Summary:	golded - offline message reader for Fidonet and Usenet
Summary(pl):	golded - program pocztowy dla Fidonetu i Usenetu
Name:		golded+
Version:	1.1.4.7
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://download.sourceforge.net/golded-plus/gps114-7.tar.bz2
Patch0:		golded-ncurses.patch
Patch1:		golded-header.patch
URL:		http://golded-plus.sourceforge.net/
BuildRequires:	gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
golded - offline message reader for Fidonet and Usenet.

%description -l pl
golded - dzia�aj�cy offline edytor wiadomo�ci dla Fidonetu i Usenetu.

%prep
%setup -q -n golded+
%patch -p0
%patch1 -p0

%build
%{__make} CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_libdir}/golded/{charset,colorset,config,template}

install bin/gedlnx	$RPM_BUILD_ROOT%{_bindir}/golded
install bin/gnlnx	$RPM_BUILD_ROOT%{_bindir}/goldnode
install bin/rddtlnx	$RPM_BUILD_ROOT%{_bindir}/rddt

install docs/*.1	$RPM_BUILD_ROOT%{_mandir}/man1

install cfgs/charset/*.chs $RPM_BUILD_ROOT%{_libdir}/golded/charset
install cfgs/charset/*.esc $RPM_BUILD_ROOT%{_libdir}/golded/charset

install cfgs/colorset/*.cfg $RPM_BUILD_ROOT%{_libdir}/golded/colorset
install cfgs/config/*.cfg $RPM_BUILD_ROOT%{_libdir}/golded/config
install cfgs/config/goldlang* $RPM_BUILD_ROOT%{_libdir}/golded/config
install cfgs/template/*.tpl $RPM_BUILD_ROOT%{_libdir}/golded/template
install cfgs/template/*.cfm $RPM_BUILD_ROOT%{_libdir}/golded/template

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/golded
%attr(755,root,root) %{_bindir}/goldnode
%attr(755,root,root) %{_bindir}/rddt
%{_mandir}/man1/*
%doc docs/*.txt docs/StyleGuide
%{_libdir}/golded/charset/*
%{_libdir}/golded/colorset/*
%{_libdir}/golded/config*
%{_libdir}/golded/template/*
