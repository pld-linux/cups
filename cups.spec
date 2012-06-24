Summary:	Common Unix Printing System	
Summary(pl):	Popularny System Druku dla Unixa
Summary(pt_BR):	Sistema Unix de Impress�o
Name:		cups
Version:	1.1.13
Release:	4
Epoch:		1
License:	GPL/LGPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Aplicaciones/Syst�me
Group(pl):	Aplikacje/System
Group(pt):	Aplica��es/Sistema
Group(pt_BR):	Aplica��es/Sistema
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Source1:	%{name}.init
Source2:	%{name}.pamd
Source3:	%{name}.logrotate
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-tmpdir.patch
Patch3:		%{name}-lp-lpr.patch
Patch4:		%{name}-options.patch
Patch5:		%{name}-pstoraster-gcc-2.96.patch
Patch6:		%{name}-ENCRYPTIONtxt.patch
URL:		http://www.cups.org/	
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	openssl-devel >= 0.9.6b
BuildRequires:	pam-devel
Prereq:		%{name}-libs = %{version}
Prereq:		/sbin/chkconfig
Provides:	lpr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	lpr
Obsoletes:	LPRng

%description 
CUPS provides a portable printing layer for UNIX�-based operating
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
CUPS dostarcza standardowy poziom drukowania dla system�w bazuj�cych
na UNIXie. CUPS u�ywa protoko�u IPP - Internet Printint Protocol jako
podstawy do zarz�dzania zadaniami i kolejkami druku.

%description -l pt_BR
O sistema Unix de impress�o (CUPS) fornece uma camada de impress�o
port�vel para os sistemas operacionais baseados no UNIX�.

%package libs
Summary:	Common Unix Printing System Libraries
Summary(pl):	Biblioteki dla CUPS
Summary(pt_BR):	Sistema Unix de Impress�o - bibliotecas para uso em clientes cups
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Obsoletes:	libcups1

%description libs
Common Unix Printing System Libraries.

%description libs -l pl
Biblioteki dla CUPS.

%description -l pt_BR libs
Bibliotecas CUPS requeridas pelos clientes CUPS.

%package devel
Summary:	Common Unix Printing System development files
Summary(pl):	Popularny System Druku dla Unixa, pliki nag��wkowe
Summary(pt_BR):	Sistema Unix de Impress�o - ambiente de desenvolvimento
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-libs = %{version}
Obsoletes:	libcups1-devel

%description devel
Common Unix Printing System development files.

%description -l pl devel
Popularny System Druku dla Unixa, pliki nag��wkowe.

%description -l pt_BR devel
Este pacote � um adicional que contem um ambiente de desenvolvimento
para a cria��o de suporte a novas impressoras e novos servi�os ao
CUPS.

%package static
Summary:	Common Unix Printing System static libraries
Summary(pl):	Popularny System Druku dla Unixa, biblioteki statyczne
Summary(pt_BR):	Common Unix Printing System - bibliotecas est�ticas
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Common Unix Printing System static libraries.

%description -l pl static
Popularny System Druku dla Unixa, biblioteki statyczne.

%description -l pt_BR static
Bibliotecas est�ticas para desenvolvimento de programas que usam as
bibliotecas do CUPS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
aclocal
autoconf
%configure \
	--with-docdir=%{_datadir}/%{name}-%{version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,logrotate.d} \
	$RPM_BUILD_ROOT/var/log/{,archiv/}cups

%{__make} DESTDIR=$RPM_BUILD_ROOT install 

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/%{name}
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/logrotate.d/%{name}

touch $RPM_BUILD_ROOT/var/log/cups/{access_log,error_log,page_log}

gzip -9nf *.txt

%clean
rm -rf $RPM_BUILD_ROOT

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

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html doc/*.css doc/images
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/*
%attr(754,root,root) /etc/rc.d/init.d/cups
%dir %{_sysconfdir}/%{name}
%attr(640,root,lp) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*.conf
%attr(640,root,lp) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*.convs
%attr(640,root,lp) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*.types
%dir %{_sysconfdir}/%{name}/certs
%dir %{_sysconfdir}/%{name}/interfaces
%dir %{_sysconfdir}/%{name}/ppd
%attr(644,root,root) %{_sysconfdir}/logrotate.d/%{name}
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
%dir %{_libdir}/cups
%dir %{_libdir}/cups/*
%attr(755,root,root)  %{_libdir}/cups/*/*
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/cups
%{_mandir}/man[158]/*
%lang(C)  %{_datadir}/locale/C/cups_C
%lang(de) %{_datadir}/locale/de/cups_de
%lang(en) %{_datadir}/locale/en/cups_en
%lang(es) %{_datadir}/locale/es/cups_es
%lang(fr) %{_datadir}/locale/fr/cups_fr
%lang(it) %{_datadir}/locale/it/cups_it
/var/spool/cups
%attr(750,root,root) %dir /var/log/archiv/cups
%attr(750,root,root) %dir /var/log/cups
%attr(640,root,root) %ghost /var/log/cups/access_log
%attr(640,root,root) %ghost /var/log/cups/error_log
%attr(640,root,root) %ghost /var/log/cups/page_log

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cups-config
%{_includedir}/cups
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
