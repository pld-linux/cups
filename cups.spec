Summary:	Common Unix Printing System	
Summary(pl):	Popularny System Druku dla Unixa
Summary(pt_BR):	Sistema Unix de Impressão
Name:		cups
Version:	1.1.14
Release:	2
Epoch:		1
License:	GPL/LGPL
Group:		Applications/System
Group(cs):	Aplikace/Systém
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/Système
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥·¥¹¥Æ¥à
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	Aplicações/Sistema
Group(pt_BR):	Aplicações/Sistema
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/óÉÓÔÅÍÁ
Group(sl):	Programi/Sistem
Group(sv):	Tillämpningar/System
Group(uk):	ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ/óÉÓÔÅÍÁ
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
na UNIXie. CUPS u¿ywa protoko³u IPP - Internet Printint Protocol jako
podstawy do zarz±dzania zadaniami i kolejkami druku.

%description -l pt_BR
O sistema Unix de impressão (CUPS) fornece uma camada de impressão
portável para os sistemas operacionais baseados no UNIX®.

%package lib
Summary:	Common Unix Printing System Libraries
Summary(pl):	Biblioteki dla CUPS
Summary(pt_BR):	Sistema Unix de Impressão - bibliotecas para uso em clientes cups
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Provides:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-libs
Obsoletes:	libcups1


%description lib
Common Unix Printing System Libraries.

%description lib -l pl
Biblioteki dla CUPS.

%description lib -l pt_BR
Bibliotecas CUPS requeridas pelos clientes CUPS.

%package image-lib
Summary:	Common Unix Printing System Libraries - images manipulation
Summary(pl):	Biblioteki dla CUPS - obs³uga formatów graficznych
Summary(pt_BR):	Sistema Unix de Impressão - bibliotecas para uso em clientes cups
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Obsoletes:	libcups1

%description image-lib
Common Unix Printing System Libraries - images manupalation.

%description image-lib -l pl
Biblioteki dla CUPS - obs³uga formatów graficznych.

%description image-lib -l pt_BR
Bibliotecas CUPS requeridas pelos clientes CUPS.

%package devel
Summary:	Common Unix Printing System development files
Summary(pl):	Popularny System Druku dla Unixa, pliki nag³ówkowe
Summary(pt_BR):	Sistema Unix de Impressão - ambiente de desenvolvimento
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-lib = %{version}
Requires:	%{name}-image-lib = %{version}
Obsoletes:	libcups1-devel

%description devel
Common Unix Printing System development files.

%description devel -l pl
Popularny System Druku dla Unixa, pliki nag³ówkowe.

%description devel -l pt_BR
Este pacote é um adicional que contem um ambiente de desenvolvimento
para a criação de suporte a novas impressoras e novos serviços ao
CUPS.

%package static
Summary:	Common Unix Printing System static libraries
Summary(pl):	Popularny System Druku dla Unixa, biblioteki statyczne
Summary(pt_BR):	Common Unix Printing System - bibliotecas estáticas
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Common Unix Printing System static libraries.

%description static -l pl
Popularny System Druku dla Unixa, biblioteki statyczne.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de programas que usam as
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
	--with-docdir=%{_libdir}/%{name}/cgi-bin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,logrotate.d} \
	$RPM_BUILD_ROOT/var/log/{,archiv/}cups

%{__make} DESTDIR=$RPM_BUILD_ROOT install 

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/%{name}
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/logrotate.d/%{name}

# for internal http browser:
cp doc/*.html	$RPM_BUILD_ROOT/%{_libdir}/%{name}/cgi-bin/
cp doc/*.css	$RPM_BUILD_ROOT/%{_libdir}/%{name}/cgi-bin/
cp doc/images/*	$RPM_BUILD_ROOT/%{_libdir}/%{name}/cgi-bin/images/

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

%post   lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig
%post   image-lib -p /sbin/ldconfig
%postun image-lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc *.gz doc/*.html doc/*.css doc/images
%doc *.gz
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
%lang(be) %{_datadir}/locale/be/cups_be
%lang(cs) %{_datadir}/locale/cs/cups_cs
%lang(de) %{_datadir}/locale/de/cups_de
%lang(en) %{_datadir}/locale/en/cups_en
%lang(es) %{_datadir}/locale/es/cups_es
%lang(fr) %{_datadir}/locale/fr/cups_fr
%lang(he) %{_datadir}/locale/he/cups_he
%lang(it) %{_datadir}/locale/it/cups_it
%lang(ru_RU) %{_datadir}/locale/ru_RU.*/cups_ru_RU.*
%lang(sv) %{_datadir}/locale/sv/cups_sv
%lang(uk) %{_datadir}/locale/uk/cups_uk
%lang(uk_UA) %{_datadir}/locale/uk_UA.*/cups_uk_UA.*
%lang(zh_CN) %{_datadir}/locale/zh_CN/cups_zh_CN
/var/spool/cups
%attr(750,root,root) %dir /var/log/archiv/cups
%attr(750,root,root) %dir /var/log/cups
%attr(640,root,root) %ghost /var/log/cups/access_log
%attr(640,root,root) %ghost /var/log/cups/error_log
%attr(640,root,root) %ghost /var/log/cups/page_log

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcups.so.*

%files image-lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcupsimage.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cups-config
%{_includedir}/cups
%{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
