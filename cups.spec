Summary:	Common Unix Printing System	
Name:		cups
Version:	1.1.4
Release:	2
Vendor:		PLD
License:	GPL/LGPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Patch0:		%{name}-chown.patch
URL:		http://www.cups.org/	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description 
CUPS provides a portable printing layer for UNIX®-based operating
systems. It has been developed by Easy Software Products to promote a
standard printing solution for all UNIX vendors and users. CUPS
provides the System V and Berkeley command-line interfaces. CUPS uses
the Internet Printing Protocol ("IPP") as the basis for managing print
jobs and queues. The Line Printer Daemon ("LPD") Server Message Block
("SMB"), and AppSocket (a.k.a. JetDirect) protocols are also supported
with reduced functionality. CUPS adds network printer browsing and
PostScript Printer Description ("PPD") based printing options to
support real-world printing under UNIX.

%package devel
Summary:	Common Unix Printing System development files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
Common Unix Printing System development files

%package static
Summary:	Common Unix Printing System static libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description static
Common Unix Printing System static libraries

%prep
%setup -q
%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT

%{__make} \
        prefix=$RPM_BUILD_ROOT \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
        BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DATADIR=$RPM_BUILD_ROOT%{_datadir}/cups \
        DOCDIR=$RPM_BUILD_ROOT%{_datadir}/doc/cups \
        INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	LOCALEDIR=$RPM_BUILD_ROOT%{_datadir}/locale \
        MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	PAMDIR=$RPM_BUILD_ROOT/etc/pam.d \
        REQUESTS=$RPM_BUILD_ROOT/var/spool/cups \
	SBINDIR=$RPM_BUILD_ROOT%{_sbindir} \
        SERVERBIN=$RPM_BUILD_ROOT%{_libdir}/cups \
	SERVERROOT=$RPM_BUILD_ROOT%{_sysconfdir}/cups \
    install 
    
%clean

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}
%attr(755,root,root) %{_libdir}/lib*.so*
%attr(755,root,root) %{_libdir}/accept
%attr(755,root,root) %{_libdir}/lpadmin
%attr(755,root,root) %{_libdir}/lpmove
%attr(755,root,root) %{_libdir}/reject
%attr(755,root,root) %{_libdir}/cups
%attr(755,root,root) %{_sbindir}
%{_datadir}/cups
%{_mandir}/man[158]
%lang(C)  %{_datadir}/locale/C/cups_C
%lang(de) %{_datadir}/locale/de/cups_de
%lang(en) %{_datadir}/locale/en/cups_en
%lang(es) %{_datadir}/locale/es/cups_es
%lang(fr) %{_datadir}/locale/fr/cups_fr
%lang(it) %{_datadir}/locale/it/cups_it

%files devel
%defattr(644,root,root,755)
%{_includedir}/cups

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
