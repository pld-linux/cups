# TODO:
# - kill CFLAGS from `cups-config --libs`
# - build/install java ext ?
# - perl BRs
# - remove obsolete /etc/cups/certs (trigger?)
#
# warning: Installed (but unpackaged) file(s) found:
#   /usr/share/applications/cups.desktop
#   /usr/share/icons/hicolor/128x128/apps/cups.png
#   /usr/share/icons/hicolor/16x16/apps/cups.png
#   /usr/share/icons/hicolor/32x32/apps/cups.png
#   /usr/share/icons/hicolor/64x64/apps/cups.png
#
# Conditional build:
%bcond_with	gnutls		# use GNU TLS for SSL/TLS support (instead of OpenSSL)
%bcond_without	dnssd
%bcond_without	php		# don't build PHP extension
%bcond_without	perl		# don't build Perl extension
%bcond_without	java
%bcond_without	python
%bcond_without	static_libs	# don't build static library
#
%include	/usr/lib/rpm/macros.perl
%define		pdir CUPS
Summary:	Common Unix Printing System
Summary(pl.UTF-8):	Ogólny system druku dla Uniksa
Summary(pt_BR.UTF-8):	Sistema Unix de Impressão
Name:		cups
Version:	1.3.4
Release:	2
Epoch:		1
License:	GPL/LGPL
Group:		Applications/Printing
Source0:	http://ftp.easysw.com/pub/cups/%{version}/%{name}-%{version}-source.tar.bz2
# Source0-md5:	4bd20d69bb083b42632346a383b6aefb
Source1:	%{name}.init
Source2:	%{name}.pamd
Source3:	%{name}.logrotate
Source4:	%{name}.mailto.conf
Patch0:		%{name}-config.patch
Patch1:		%{name}-lp-lpr.patch
Patch2:		%{name}-options.patch
Patch3:		%{name}-man_pages_linking.patch
Patch4:		%{name}-nostrip.patch
Patch5:		%{name}-templates.patch
Patch6:		%{name}-certs_FHS.patch
Patch7:		%{name}-direct_usb.patch
URL:		http://www.cups.org/
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_dnssd:BuildRequires:	avahi-compat-libdns_sd-devel}
BuildRequires:	dbus-devel
BuildRequires:	glibc-headers
%{?with_gnutls:BuildRequires:	gnutls-devel}
BuildRequires:	krb5-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openslp-devel
%{!?with_gnutls:BuildRequires:	openssl-devel}
BuildRequires:	pam-devel
%{?with_php:BuildRequires:	php-devel >= 4:5.0.0}
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.344
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.77.3
Requires:	rc-scripts
Obsoletes:	printingdaemon
Provides:	printingdaemon
Conflicts:	ghostscript < 7.05.4
Conflicts:	logrotate < 3.7-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
CUPS provides a portable printing layer for UNIX-based operating
systems. It has been developed by Easy Software Products to promote a
standard printing solution for all UNIX vendors and users. CUPS
provides the System V and Berkeley command-line interfaces. CUPS uses
the Internet Printing Protocol ("IPP") as the basis for managing print
jobs and queues. The Line Printer Daemon ("LPD") Server Message Block
("SMB"), and AppSocket (a.k.a. JetDirect) protocols are also supported
with reduced functionality. CUPS adds network printer browsing and
PostScript Printer Description ("PPD") based printing options to
support real-world printing under UNIX.

%description -l pl.UTF-8
CUPS dostarcza standardowy poziom drukowania dla systemów uniksowych.
CUPS używa protokołu IPP - Internet Printint Protocol jako podstawy do
zarządzania zadaniami i kolejkami druku. W ograniczonym zakresie
obsługiwane są także protokoły LPD (Line Printer Daemon), SMB (Server
Message Block) i AppSocket (znany także jako JetDirect). CUPS
udostępnia przeglądanie drukarek sieciowych i opcje drukowania oparte
na PPD (PostScript Printer Description) do obsługi rzeczywistych
drukarek.

%description -l pt_BR.UTF-8
O sistema Unix de impressão (CUPS) fornece uma camada de impressão
portável para os sistemas operacionais baseados no UNIX®.

%package lib
Summary:	Common Unix Printing System Libraries
Summary(pl.UTF-8):	Biblioteki dla CUPS
Summary(pt_BR.UTF-8):	Sistema Unix de Impressão - bibliotecas para uso em clientes cups
Group:		Libraries
Provides:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	cups-libs
Obsoletes:	libcups1

%description lib
Common Unix Printing System Libraries.

%description lib -l pl.UTF-8
Biblioteki dla CUPS.

%description lib -l pt_BR.UTF-8
Bibliotecas CUPS requeridas pelos clientes CUPS.

%package clients
Summary:	Common Unix Printing System Clients
Summary(pl.UTF-8):	Aplikacje klienckie dla CUPS
Group:		Applications/Printing
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	printingclient
Provides:	printingclient

%description clients
Common Unix Printing System Clients.

%description clients -l pl.UTF-8
Aplikacje klienckie dla CUPS.

%package image-lib
Summary:	Common Unix Printing System Libraries - images manipulation
Summary(pl.UTF-8):	Biblioteki dla CUPS - obsługa formatów graficznych
Summary(pt_BR.UTF-8):	Sistema Unix de Impressão - bibliotecas para uso em clientes cups
Group:		Libraries
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Obsoletes:	libcups1

%description image-lib
Common Unix Printing System Libraries - images manipalation.

%description image-lib -l pl.UTF-8
Biblioteki dla CUPS - obsługa formatów graficznych.

%description image-lib -l pt_BR.UTF-8
Bibliotecas CUPS requeridas pelos clientes CUPS.

%package devel
Summary:	Common Unix Printing System development files
Summary(pl.UTF-8):	Ogólny system druku dla Uniksa - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Sistema Unix de Impressão - ambiente de desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-image-lib = %{epoch}:%{version}-%{release}
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
# for libcups
%{?with_gnutls:Requires:	gnutls-devel}
Requires:	krb5-devel
%{!?with_gnutls:Requires:	openssl-devel}
Requires:	zlib-devel
# for libcupsimage
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel
Obsoletes:	libcups1-devel

%description devel
Common Unix Printing System development files.

%description devel -l pl.UTF-8
Ogólny system druku dla Uniksa - pliki nagłówkowe.

%description devel -l pt_BR.UTF-8
Este pacote é um adicional que contem um ambiente de desenvolvimento
para a criação de suporte a novas impressoras e novos serviços ao
CUPS.

%package static
Summary:	Common Unix Printing System static libraries
Summary(pl.UTF-8):	Ogólny system druku dla Uniksa - biblioteki statyczne
Summary(pt_BR.UTF-8):	Common Unix Printing System - bibliotecas estáticas
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Common Unix Printing System static libraries.

%description static -l pl.UTF-8
Ogólny system druku dla Uniksa - biblioteki statyczne.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de programas que usam as
bibliotecas do CUPS.

%package -n perl-cups
Summary:	Perl module for CUPS
Summary(pl.UTF-8):	Moduł Perla CUPS
Group:		Development/Languages/Perl
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description -n perl-cups
Perl module for Common Unix Printing System.

%description -n perl-cups -l pl.UTF-8
Moduł Perla do ogólnego systemu druku dla Uniksa.

%package -n php-cups
Summary:	PHP module for CUPS
Summary(pl.UTF-8):	Moduł PHP CUPS
Group:		Development/Languages/PHP
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
%{?requires_php_extension}
Requires:	/etc/php/conf.d
Requires:	php-common >= 4:5.0.0

%description -n php-cups
PHP module for Common Unix Printing System.

%description -n php-cups -l pl.UTF-8
Moduł PHP do ogólnego systemu druku dla Uniksa.

%package backend-usb
Summary:	USB backend for CUPS
Summary(pl.UTF-8):	Backend USB dla CUPS-a
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-usb
This package allow CUPS printing on USB printers.

%description backend-usb -l pl.UTF-8
Ten pakiet umożliwia drukowanie z poziomu CUPS-a na drukarkach USB.

%package backend-serial
Summary:	Serial port backend for CUPS
Summary(pl.UTF-8):	Backend obsługujący porty szeregowe dla CUPS-a
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-serial
This package allow CUPS printing on printers connected by serial
ports.

%description backend-serial -l pl.UTF-8
Ten pakiet umożliwia drukowanie z poziomu CUPS-a na drukarkach
podłączonych do portów szeregowych.

%package backend-parallel
Summary:	Parallel port backend for CUPS
Summary(pl.UTF-8):	Backend obsługujący porty równoległe dla CUPS-a
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-parallel
This package allow CUPS printing on printers connected by parallel
ports.

%description backend-parallel -l pl.UTF-8
Ten pakiet umożliwia drukowanie z poziomu CUPS-a na drukarkach
podłączonych do portów równoległych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%{__aclocal} -I config-scripts
%{__autoconf}
%configure \
	--libdir=%{_ulibdir} \
	--enable-shared \
	--with-cups-user=lp \
	--with-cups-group=sys \
	--with-system-groups=sys \
	--with-printcap=/etc/printcap \
	%{?with_static_libs:--enable-static} \
	--enable-ssl \
	--%{?with_gnutls:dis}%{!?with_gnutls:en}able-openssl \
	--%{!?with_gnutls:dis}%{?with_gnutls:en}able-gnutls \
	--%{!?with_dnssd:dis}%{?with_dnssd:en}able-dnssd \
	--disable-cdsassl \
	--enable-dbus \
	%{?debug:--enable-debug} \
	--with-docdir=%{_ulibdir}/%{name}/cgi-bin \
	--with-config-file-perm=0640 \
	--with-log-file-perm=0640 \
	%{?with_dnssd:--with-dnssd-libs=x} \
	%{?with_dnssd:--with-dnssd-includes=x} \
	%{?with_php:--with-php} \
	%{?with_perl:--with-perl} \
	%{?with_java:--with-java} \
	%{?with_php:--with-python}

%{__make}

%{__perl} -pi -e 's#-I\.\.\/\.\.#-I../.. -I../../cups#g' scripting/php/Makefile
%{?with_php:%{__make} -C scripting/php PHPCONFIG=%{_bindir}/php-config}

%if %{with perl}
cd scripting/perl
%{__perl} -pi -e 's@-lcups@-L../../cups $1@' Makefile.PL
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags} -I../.."
# avoid rpaths generated by MakeMaker
%{__perl} -pi -e 's@LD_RUN_PATH="\$\(LD_RUN_PATH\)" @@' Makefile

%{__make}
cd ../..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,logrotate.d,security} \
	$RPM_BUILD_ROOT/var/run/cups \
	$RPM_BUILD_ROOT/var/log/{,archive/}cups

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT \
	CUPS_USER=$(id -u) \
	CUPS_GROUP=$(id -g)

if [ "%{_lib}" != "lib" ] ; then
	install -d $RPM_BUILD_ROOT%{_libdir}
	mv $RPM_BUILD_ROOT%{_ulibdir}/*.so* $RPM_BUILD_ROOT%{_libdir}
	mv $RPM_BUILD_ROOT%{_ulibdir}/*.a $RPM_BUILD_ROOT%{_libdir}
fi

%if %{with php}
%{__make} -C scripting/php install \
	PHPDIR=$RPM_BUILD_ROOT%{php_extensiondir}
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d
cat > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/phpcups.ini << EOF
; Enable phpcups extension module
extension=phpcups.so
EOF
%endif

%if %{with perl}
%{__make} -C scripting/perl install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/%{name}
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/logrotate.d/%{name}
install %{SOURCE4}      $RPM_BUILD_ROOT/etc/cups/mailto.conf

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/%{name}/model/*.ppd

touch $RPM_BUILD_ROOT/var/log/cups/{access_log,error_log,page_log}
touch $RPM_BUILD_ROOT/etc/security/blacklist.cups
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{classes,printers,client}.conf

# windows drivers can be put there.
install -d $RPM_BUILD_ROOT%{_datadir}/cups/drivers

# dirs for gimp-print-cups-4.2.7-1
install -d $RPM_BUILD_ROOT%{_datadir}/cups/model/{C,da,en_GB,fr,nb,pl,sv}

touch $RPM_BUILD_ROOT/var/cache/cups/help.index
touch $RPM_BUILD_ROOT/var/cache/cups/{job,remote}.cache
touch $RPM_BUILD_ROOT/var/cache/cups/ppds.dat
install -d $RPM_BUILD_ROOT%{_sysconfdir}/cups/ssl

# links to enable/disable (compatibility!)
ln -s accept $RPM_BUILD_ROOT%{_sbindir}/enable
ln -s accept $RPM_BUILD_ROOT%{_sbindir}/disable

# fix/update locale names
install -d $RPM_BUILD_ROOT%{_datadir}/locale/{nb,zh_CN}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no/cups_no.po,nb/cups_nb.po}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh/cups_zh.po,zh_CN/cups_zh_CN.po}

# check-files cleanup
rm -rf $RPM_BUILD_ROOT%{_mandir}/{,es/,fr/}cat?
rm -rf $RPM_BUILD_ROOT/''etc/{init.d,rc?.d}/*
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/cupsd.conf.default

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add cups
%service cups restart "cups daemon"

%preun
if [ "$1" = "0" ]; then
	%service cups stop
	/sbin/chkconfig --del cups
fi

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig
%post	image-lib -p /sbin/ldconfig
%postun	image-lib -p /sbin/ldconfig

%post -n php-cups
%php_webserver_restart

%postun -n php-cups
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
#%doc *.gz doc/*.html doc/*.css doc/images
%doc *.txt
%attr(640,root,root) %config %verify(not md5 mtime size) /etc/pam.d/*
%attr(754,root,root) /etc/rc.d/init.d/cups
/etc/dbus-1/system.d/cups.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/classes.conf
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/cupsd.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/printers.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/mailto.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/snmp.conf
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.convs
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.types
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.cups
%dir %attr(700,root,lp) %{_sysconfdir}/%{name}/ssl
%dir %{_sysconfdir}/%{name}/interfaces
%dir %attr(755,root,lp) %{_sysconfdir}/%{name}/ppd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}
%attr(4755,lp,root) %{_bindir}/lppasswd
%attr(755,root,root) %{_bindir}/cupstestppd
%attr(755,root,root) %{_bindir}/cupstestdsc
%attr(755,root,root) %{_sbindir}/cupsctl
%attr(755,root,root) %{_sbindir}/cupsd
%attr(755,root,root) %{_sbindir}/cupsfilter

%dir %{_ulibdir}/cups
%dir %{_ulibdir}/cups/*
%{_ulibdir}/cups/cgi-bin/help
%{_ulibdir}/cups/cgi-bin/images
%attr(755,root,root) %{_ulibdir}/cups/cgi-bin/*.cgi
%{_ulibdir}/cups/cgi-bin/*.css
%{_ulibdir}/cups/cgi-bin/*.html
%{_ulibdir}/cups/cgi-bin/*.ico
%{_ulibdir}/cups/cgi-bin/*.txt
%lang(de) %{_ulibdir}/cups/cgi-bin/de
%lang(es) %{_ulibdir}/cups/cgi-bin/es
%lang(et) %{_ulibdir}/cups/cgi-bin/et
%lang(fr) %{_ulibdir}/cups/cgi-bin/fr
%lang(he) %{_ulibdir}/cups/cgi-bin/he
%lang(it) %{_ulibdir}/cups/cgi-bin/it
%lang(ja) %{_ulibdir}/cups/cgi-bin/ja
%lang(pl) %{_ulibdir}/cups/cgi-bin/pl
%lang(sv) %{_ulibdir}/cups/cgi-bin/sv
%lang(zh_TW) %{_ulibdir}/cups/cgi-bin/zh_TW

%exclude %{_ulibdir}/cups/backend/usb
%exclude %{_ulibdir}/cups/backend/serial
%exclude %{_ulibdir}/cups/backend/parallel
%attr(755,root,root) %{_ulibdir}/cups/backend/*
%attr(755,root,root) %{_ulibdir}/cups/daemon/*
%attr(755,root,root) %{_ulibdir}/cups/filter/*
%attr(755,root,root) %{_ulibdir}/cups/monitor/*
%attr(755,root,root) %{_ulibdir}/cups/notifier/*

%{_datadir}/cups/banners
%{_datadir}/cups/charsets
%{_datadir}/cups/data
%{_datadir}/cups/drivers
%{_datadir}/cups/fonts
%dir %{_datadir}/cups/model
%{_datadir}/cups/model/*.ppd.gz
# dirs for gimp-print-cups-4.2.7-1
%dir %{_datadir}/cups/model/C
%lang(da) %dir %{_datadir}/cups/model/da
%lang(en_GB) %dir %{_datadir}/cups/model/en_GB
%lang(fr) %dir %{_datadir}/cups/model/fr
%lang(nb) %dir %{_datadir}/cups/model/nb
%lang(pl) %dir %{_datadir}/cups/model/pl
%lang(sv) %dir %{_datadir}/cups/model/sv

%dir %{_datadir}/cups/templates
%{_datadir}/cups/templates/*.tmpl
%lang(de) %{_datadir}/cups/templates/de
%lang(es) %{_datadir}/cups/templates/es
%lang(et) %{_datadir}/cups/templates/et
%lang(fr) %{_datadir}/cups/templates/fr
%lang(he) %{_datadir}/cups/templates/he
%lang(it) %{_datadir}/cups/templates/it
%lang(ja) %{_datadir}/cups/templates/ja
%lang(pl) %{_datadir}/cups/templates/pl
%lang(sv) %{_datadir}/cups/templates/sv
%lang(zh_TW) %{_datadir}/cups/templates/zh_TW
%{_mandir}/man1/cupstestppd.1*
%{_mandir}/man1/cupstestdsc.1*
%{_mandir}/man1/lppasswd.1*
%{_mandir}/man7/backend.7*
%{_mandir}/man7/filter.7*
%{_mandir}/man[58]/*

%dir %attr(775,root,lp) /var/cache/cups
%dir %attr(755,root,lp) /var/lib/cups
%dir %attr(511,lp,sys) /var/lib/cups/certs
%dir %attr(755,root,lp) /var/run/cups
%dir %attr(710,root,lp) /var/spool/cups
%dir %attr(1770,root,lp) /var/spool/cups/tmp
%attr(600,lp,lp) %ghost /var/cache/cups/help.index
%attr(640,root,lp) %ghost /var/cache/cups/job.cache
%attr(600,lp,lp) %ghost /var/cache/cups/ppds.dat
%attr(640,root,lp) %ghost /var/cache/cups/remote.cache
%attr(750,root,logs) %dir /var/log/archive/cups
%attr(750,root,logs) %dir /var/log/cups
%attr(640,root,logs) %ghost /var/log/cups/access_log
%attr(640,root,logs) %ghost /var/log/cups/error_log
%attr(640,root,logs) %ghost /var/log/cups/page_log

%files lib
%defattr(644,root,root,755)
%dir %attr(755,root,lp) %{_sysconfdir}/%{name}
%attr(755,root,root) %{_libdir}/libcups.so.*
%dir %{_datadir}/cups
%{_datadir}/cups/charmaps
%lang(da) %{_datadir}/locale/da/cups_da.po
%lang(de) %{_datadir}/locale/de/cups_de.po
%lang(es) %{_datadir}/locale/es/cups_es.po
%lang(et) %{_datadir}/locale/et/cups_et.po
%lang(fi) %{_datadir}/locale/fi/cups_fi.po
%lang(fr) %{_datadir}/locale/fr/cups_fr.po
%lang(he) %{_datadir}/locale/he/cups_he.po
%lang(it) %{_datadir}/locale/it/cups_it.po
%lang(ko) %{_datadir}/locale/ko/cups_ko.po
%lang(ja) %{_datadir}/locale/ja/cups_ja.po
%lang(nl) %{_datadir}/locale/nl/cups_nl.po
%lang(nb) %{_datadir}/locale/nb/cups_nb.po
%lang(pl) %{_datadir}/locale/pl/cups_pl.po
%lang(pt) %{_datadir}/locale/pt/cups_pt.po
%lang(pt_BR) %{_datadir}/locale/pt_BR/cups_pt_BR.po
%lang(ru) %{_datadir}/locale/ru/cups_ru.po
%lang(sv) %{_datadir}/locale/sv/cups_sv.po
%lang(zh_CN) %{_datadir}/locale/zh_CN/cups_zh_CN.po
%lang(zh_TW) %{_datadir}/locale/zh_TW/cups_zh_TW.po

%files clients
%defattr(644,root,root,755)
%attr(644,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/client.conf
%attr(755,root,root) %{_bindir}/cancel
%attr(755,root,root) %{_bindir}/lp
%attr(755,root,root) %{_bindir}/lpoptions
%attr(755,root,root) %{_bindir}/lpq
%attr(755,root,root) %{_bindir}/lpr
%attr(755,root,root) %{_bindir}/lprm
%attr(755,root,root) %{_bindir}/lpstat
%attr(755,root,root) %{_sbindir}/accept
%attr(755,root,root) %{_sbindir}/cupsaddsmb
%attr(755,root,root) %{_sbindir}/cupsenable
%attr(755,root,root) %{_sbindir}/cupsdisable
%attr(755,root,root) %{_sbindir}/disable
%attr(755,root,root) %{_sbindir}/enable
%attr(755,root,root) %{_sbindir}/lpadmin
%attr(755,root,root) %{_sbindir}/lpc
%attr(755,root,root) %{_sbindir}/lpinfo
%attr(755,root,root) %{_sbindir}/lpmove
%attr(755,root,root) %{_sbindir}/reject
%{_mandir}/man1/cancel.1*
%{_mandir}/man1/lp.1*
%{_mandir}/man1/lpoptions.1*
%{_mandir}/man1/lpq.1*
%{_mandir}/man1/lpr.1*
%{_mandir}/man1/lprm.1*
%{_mandir}/man1/lpstat.1*
#%lang(fr) %{_mandir}/fr/man1/cancel.1*
#%lang(fr) %{_mandir}/fr/man1/lp.1*
#%lang(fr) %{_mandir}/fr/man1/lpoptions.1*
#%lang(fr) %{_mandir}/fr/man1/lpq.1*
#%lang(fr) %{_mandir}/fr/man1/lpr.1*
#%lang(fr) %{_mandir}/fr/man1/lprm.1*
#%lang(fr) %{_mandir}/fr/man1/lpstat.1*
#%lang(es) %{_mandir}/es/man1/lp.1*
#%lang(es) %{_mandir}/es/man1/lpoptions.1*
#%lang(es) %{_mandir}/es/man1/lpq.1*
#%lang(es) %{_mandir}/es/man1/lpr.1*
#%lang(es) %{_mandir}/es/man1/lprm.1*
#%lang(es) %{_mandir}/es/man1/lpstat.1*

%files image-lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcupsimage.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cups-config
%attr(755,root,root) %{_libdir}/libcups.so
%attr(755,root,root) %{_libdir}/libcupsimage.so
%{_includedir}/cups
%{_mandir}/man1/cups-config.1*
#%lang(fr) %{_mandir}/fr/man1/cups-config.1*
#%lang(es) %{_mandir}/es/man1/cups-config.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcups.a
%{_libdir}/libcupsimage.a
%endif

%if %{with perl}
%files -n perl-cups
%defattr(644,root,root,755)
%{perl_vendorarch}/CUPS.pm
%dir %{perl_vendorarch}/auto/CUPS
%{perl_vendorarch}/auto/CUPS/CUPS.bs
%{perl_vendorarch}/auto/CUPS/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/CUPS/CUPS.so
%{_mandir}/man3/CUPS.3pm*
%endif

%if %{with php}
%files -n php-cups
%defattr(644,root,root,755)
%doc scripting/php/README
%attr(755,root,root) %{php_extensiondir}/phpcups.so
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/phpcups.ini
%endif

%files backend-usb
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/usb

%files backend-serial
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/serial

%files backend-parallel
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/parallel
