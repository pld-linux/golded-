Summary:	golded - offline message reader for Fidonet and Usenet.
Summary(pl):	golded - program pocztowy [dla fidonetu i usenetu]
Name:		golded+
Version:	1.1.4.7
Release:	1
License:	GPL
Group:		Applications/Mail
URL:		http://golded-plus.sourceforge.net
Source0:	http://download.sourceforge.net/golded-plus/gps114-7.tar.bz2
Patch0:		golded-ncurses.patch
Patch1:		golded-header.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
golded - offline message reader for Fidonet and Usenet.

%prep
%setup -q -n golded+
%patch -p0
%patch1 -p0

%build
%{__make} CC="gcc %{rpmcflags} -Wall" -j 8

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_libdir}/golded/charset
install -d $RPM_BUILD_ROOT/%{_libdir}/golded/colorset
install -d $RPM_BUILD_ROOT/%{_libdir}/golded/config
install -d $RPM_BUILD_ROOT/%{_libdir}/golded/template

install -d $RPM_BUILD_ROOT/%{_mandir}/man1

install bin/gedlnx	$RPM_BUILD_ROOT%{_bindir}/golded
install bin/gnlnx	$RPM_BUILD_ROOT%{_bindir}/goldnode
install bin/rddtlnx	$RPM_BUILD_ROOT%{_bindir}/rddt

gzip -9nf docs/*.1
install docs/*.1.gz	$RPM_BUILD_ROOT%{_mandir}/man1/

gzip -9nf docs/*.txt
gzip -9nf docs/StyleGuide

install cfgs/charset/*.chs $RPM_BUILD_ROOT/%{_libdir}/golded/charset/
install cfgs/charset/*.esc $RPM_BUILD_ROOT/%{_libdir}/golded/charset/

install cfgs/colorset/*.cfg $RPM_BUILD_ROOT/%{_libdir}/golded/colorset/
install cfgs/config/*.cfg $RPM_BUILD_ROOT/%{_libdir}/golded/config/
install cfgs/config/goldlang* $RPM_BUILD_ROOT/%{_libdir}/golded/config/
install cfgs/template/*.tpl $RPM_BUILD_ROOT/%{_libdir}/golded/template/
install cfgs/template/*.cfm $RPM_BUILD_ROOT/%{_libdir}/golded/template/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/golded
%attr(755,root,root) %{_bindir}/goldnode
%attr(755,root,root) %{_bindir}/rddt
%{_mandir}/man1/*
%doc docs/*.txt.gz docs/StyleGuide.gz
%{_libdir}/golded/charset/*
%{_libdir}/golded/colorset/*
%{_libdir}/golded/config*
%{_libdir}/golded/template/*
