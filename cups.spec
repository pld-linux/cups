Summary:	Common Unix Printing System	
Summary(pl):	Popularny System Druku dla Unixa
Name:		cups
Version:	1.1.9
Release:	1
License:	GPL/LGPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-1-source.tar.bz2
Source1:	%{name}.init
Source2:	%{name}.pamd
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
Requires:	%{name}-libs = %{version}
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

%package libs
Summary:	Common Unix Printing System Libraries
Group:		Development/Libraries

%description libs
Common Unix Printing System Libraries

%package devel
Summary:	Common Unix Printing System development files
Summary(pl):	Popularny System Druku dla Unixa, pliki nag³ówkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-libs = %{version}

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
%patch0 -p1
%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install 

install -d		$RPM_BUILD_ROOT/%{_sysconfdir}/{rc.d/init.d,pam.d}
install %{SOURCE1}	$RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/cups
install %{SOURCE2}	$RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/cups

gzip -9nf *.txt

%post
/sbin/chkconfig --add cups
if [ -f /var/lock/subsys/cups ]; then
        /etc/rc.d/init.d/cups restart 1>&2
else
        echo "Run \"/etc/rc.d/init.d/cups start\" to start cups daemon."
fi
		
%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/cups ]; then
		/etc/rc.d/init.d/cups stop 1>&2
	fi
	/sbin/chkconfig --del cups
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html doc/*.css doc/*.pdf doc/images
%attr(4755,lp,root) %{_bindir}/lppasswd
%attr(755,root,root) %{_bindir}/cancel
%attr(755,root,root) %{_bindir}/disable
%attr(755,root,root) %{_bindir}/enable
%attr(755,root,root) %{_bindir}/lp
%attr(755,root,root) %{_bindir}/lpoptions
%attr(755,root,root) %{_bindir}/lpq
%attr(755,root,root) %{_bindir}/lpr
%attr(755,root,root) %{_bindir}/lprm
%attr(755,root,root) %{_bindir}/lpstat
%attr(755,root,root) %{_libdir}/cups
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/pam.d/*
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/cups
%attr(640,root,lp) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cups/*.conf
%attr(640,root,lp) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cups/*.convs
%attr(640,root,lp) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cups/*.types
%{_sysconfdir}/cups/certs
%{_sysconfdir}/cups/interfaces
%{_sysconfdir}/cups/ppd
%{_docdir}/cups
%{_datadir}/cups
%{_mandir}/man[158]/*
%lang(C)  %{_datadir}/locale/C/cups_C
%lang(de) %{_datadir}/locale/de/cups_de
%lang(en) %{_datadir}/locale/en/cups_en
%lang(es) %{_datadir}/locale/es/cups_es
%lang(fr) %{_datadir}/locale/fr/cups_fr
%lang(it) %{_datadir}/locale/it/cups_it
/var/log/cups
/var/spool/cups

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so*

%files devel
%defattr(644,root,root,755)
%{_includedir}/cups
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
