Summary:	Common Unix Printing System	
Summary(pl):	Popularny System Druku dla Unixa
Name:		cups
Version:	1.1.6
Release:	1
License:	GPL/LGPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Source1:	%{name}.init
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
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

%description -l pl
CUPS dostarcza standardowy poziom drukowania dla systemów bazuj±cych
na UNIXie. CUPS u¿ywa protoko³u IPP - Internet Printint Protocol
jako podstawy do zarz±dzania zadaniami i kolejkami druku.

%package devel
Summary:	Common Unix Printing System development files
Summary(pl):	Popularny System Druku dla Unixa, pliki nag³ówkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Common Unix Printing System development files

%description -l pl devel
Popularny System Druku dla Unixa, pliki nag³ówkowe
 
%package static
Summary:	Common Unix Printing System static libraries
Summary(pl):	Popularny System Druku dla Unixa, biblioteki statyczne
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Common Unix Printing System static libraries

%description -l pl static
Popularny System Druku dla Unixa, biblioteki statyczne
 
%prep
%setup -q

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

install -d $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d
install %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/cups

%find_lang %{name}

gzip -9nf *.txt

%post
/sbin/chkconfig --add cups
    
%preun
/sbin/chkconfig --del cups

%clean
rm -f $RPM_BUILD_ROOT

%files  -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}
%attr(755,root,root) %{_libdir}/lib*.so*
%attr(755,root,root) %{_libdir}/accept
%attr(755,root,root) %{_libdir}/lpadmin
%attr(755,root,root) %{_libdir}/lpmove
%attr(755,root,root) %{_libdir}/reject
%attr(755,root,root) %{_libdir}/cups
%attr(755,root,root) %{_sbindir}
%lang(C)  %{_datadir}/locale/C/cups_C
%lang(de) %{_datadir}/locale/de/cups_de
%lang(en) %{_datadir}/locale/en/cups_en
%lang(es) %{_datadir}/locale/es/cups_es
%lang(fr) %{_datadir}/locale/fr/cups_fr
%lang(it) %{_datadir}/locale/it/cups_it
%{_sysconfdir}/pam.d
%{_sysconfdir}/cups/certs
%{_sysconfdir}/cups/interfaces
%{_sysconfdir}/cups/ppd
%config(noreplace) %{_sysconfdir}/cups/*.conf
%config(noreplace) %{_sysconfdir}/cups/*.convs
%config(noreplace) %{_sysconfdir}/cups/*.types
%{_sysconfdir}/rc.d/init.d/cups
%{_docdir}/cups
%{_datadir}/cups
%{_mandir}/man[158]
/var/log/cups
/var/spool/cups

%files devel
%defattr(644,root,root,755)
%{_includedir}/cups

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
