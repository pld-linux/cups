#
# Conditional build:
%bcond_with	gnutls		# use GNU TLS for SSL/TLS support
%bcond_with	dnssd		# DNS Service Discovery support via dns_sd API
%bcond_without	avahi		# DNS Service Discovery support via Avahi
%bcond_without	gssapi		# GSSAPI support
%bcond_with	lspp		# audit and SELinux label support (lspp patch)
%bcond_with	tcp_wrappers	# tcp_wrappers/libwrap support
%bcond_without	static_libs	# static library
%bcond_without	systemd		# systemd

%if %{with dnssd}
%undefine	with_avahi
%endif

Summary(pl.UTF-8):	Ogólny system druku dla Uniksa
Summary(pt_BR.UTF-8):	Sistema Unix de Impressão
Name:		cups
Version:	2.4.12
Release:	1
Epoch:		1
License:	LGPL v2 (libraries), GPL v2 (the rest)
Group:		Applications/Printing
Source0:	https://github.com/OpenPrinting/cups/releases/download/v%{version}/cups-%{version}-source.tar.gz
# Source0-md5:	1f9281c661b95acc7925a220919210e2
Source1:	%{name}.init
Source2:	%{name}.pamd
Source3:	%{name}.logrotate
Source4:	%{name}.mailto.conf
Source5:	%{name}-lpd.inetd
Source6:	%{name}-modprobe.conf
Source7:	%{name}.tmpfiles
Patch0:		%{name}-config.patch
Patch2:		%{name}-options.patch
Patch3:		%{name}-man_pages_linking.patch
Patch4:		%{name}-nostrip.patch
Patch5:		%{name}-certs_FHS.patch
Patch6:		%{name}-direct_usb.patch
Patch7:		%{name}-no-polluted-krb5config.patch
Patch9:		%{name}-verbose-compilation.patch
Patch10:	%{name}-peercred.patch
Patch11:	%{name}-usb.patch
Patch12:	%{name}-desktop.patch
Patch15:	reactivate_recommended_driver.patch
Patch16:	read-embedded-options-from-incoming-postscript-and-add-to-ipp-attrs.patch
Patch102:	cups-banners.patch
Patch103:	cups-pid.patch
Patch104:	cups-eggcups.patch
Patch105:	cups-driverd-timeout.patch
Patch107:	cups-res_init.patch
Patch108:	cups-filter-debug.patch
Patch110:	cups-dnssd-deviceid.patch

Patch113:	cups-dymo-deviceid.patch
Patch114:	cups-freebind.patch
Patch115:	cups-ipp-multifile.patch
Patch116:	cups-web-devices-timeout.patch
Patch117:	cups-lspp.patch
URL:		https://openprinting.github.io/cups/
BuildRequires:	acl-devel
%{?with_lspp:BuildRequires:	audit-libs-devel}
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
%{?with_dnssd:BuildRequires:	avahi-compat-libdns_sd-devel}
%{?with_avahi:BuildRequires:	avahi-devel}
BuildRequires:	dbus-devel
%{?with_gnutls:BuildRequires:	gnutls-devel}
%{?with_gssapi:BuildRequires:	heimdal-devel}
BuildRequires:	libapparmor-devel
BuildRequires:	libpaper-devel
%{?with_lspp:BuildRequires:	libselinux-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libusb-devel >= 1.0
%{?with_tcp_wrappers:BuildRequires:	libwrap-devel}
%{!?with_gnutls:BuildRequires:	openssl-devel}
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.641
BuildRequires:	snapd-glib-2-devel
%{?with_systemd:BuildRequires:	systemd-devel}
BuildRequires:	zlib-devel
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Requires:	%{name}-ppdc = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.77.3
Requires:	rc-scripts
Requires:	systemd-units >= 38
Suggests:	cups-filters
Suggests:	poppler-progs
Provides:	printingdaemon
Obsoletes:	printingdaemon
Conflicts:	ghostscript < 7.05.4
Conflicts:	hplip < 3.13.11
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

%package backend-usb
Summary:	USB backend for CUPS
Summary(pl.UTF-8):	Backend USB dla CUPS-a
License:	GPL v2
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-usb
This package allow CUPS printing on USB printers.

%description backend-usb -l pl.UTF-8
Ten pakiet umożliwia drukowanie z poziomu CUPS-a na drukarkach USB.

%package lpd
Summary:	LPD compatibility support for CUPS print server
Summary(pl.UTF-8):	Wsparcie dla LPD w serwerze wydruków CUPS
License:	GPL v2
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	rc-inetd

%description lpd
LPD compatibility support for CUPS print server.

%description lpd -l pl.UTF-8
Wsparcie dla LPD w serwerze wydruków CUPS.

%package ppdc
Summary:	Common Unix Printing System - PPD manipulation utilities
Summary(pl.UTF-8):	Narzędzia CUPS do operacji na plikach PPD
License:	GPL v2
Group:		Applications/Printing
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description ppdc
This package provides utilities to generate and manipulate PPD files.

%description ppdc -l pl.UTF-8
Ten pakiet zawiera narzędzia do generowania i operowania na plikach
PPD.

%package clients
Summary:	Common Unix Printing System Clients
Summary(pl.UTF-8):	Aplikacje klienckie dla CUPS
License:	GPL v2
Group:		Applications/Printing
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Provides:	printingclient
Obsoletes:	printingclient

%description clients
Common Unix Printing System Clients.

%description clients -l pl.UTF-8
Aplikacje klienckie dla CUPS.

%package lib
Summary:	Common Unix Printing System Libraries
Summary(pl.UTF-8):	Biblioteki dla CUPS
Summary(pt_BR.UTF-8):	Sistema Unix de Impressão - bibliotecas para uso em clientes cups
License:	LGPL v2
Group:		Libraries
Provides:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	cups-libs < 1:1.1.14-2
Obsoletes:	libcups1 < 1:2

%description lib
Common Unix Printing System Libraries.

%description lib -l pl.UTF-8
Biblioteki dla CUPS.

%description lib -l pt_BR.UTF-8
Bibliotecas CUPS requeridas pelos clientes CUPS.

%package image-lib
Summary:	Common Unix Printing System Libraries - images manipulation
Summary(pl.UTF-8):	Biblioteki dla CUPS - obsługa formatów graficznych
Summary(pt_BR.UTF-8):	Sistema Unix de Impressão - bibliotecas para uso em clientes cups
License:	LGPL v2
Group:		Libraries
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Obsoletes:	libcups1 < 1:2

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
License:	LGPL v2
Group:		Development/Libraries
Requires:	%{name}-image-lib = %{epoch}:%{version}-%{release}
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
%{?with_avahi:Requires:	avahi-devel}
%{?with_gnutls:Requires: gnutls-devel}
%{!?with_gnutls:Requires: openssl-devel}
Obsoletes:	libcups1-devel < 1:2

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
License:	LGPL v2
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Common Unix Printing System static libraries.

%description static -l pl.UTF-8
Ogólny system druku dla Uniksa - biblioteki statyczne.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de programas que usam as
bibliotecas do CUPS.

%prep
%setup -q
%patch -P0 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
# why it hasn't been merged for so long (and why no other distro uses it)
#%%patch -P6 -p1
%patch -P7 -p1
%patch -P9 -p1
%patch -P10 -p1
# why it hasn't been merged for so long (and why no other distro uses it)
#%%patch -P11 -p1
%patch -P12 -p1
%patch -P15 -p1
%patch -P16 -p1

%patch -P102 -p1
%patch -P103 -p1
%patch -P104 -p1
%patch -P105 -p1
%patch -P107 -p1
%patch -P108 -p1
%patch -P110 -p1

%patch -P113 -p1
%patch -P114 -p1
%patch -P115 -p1
%patch -P116 -p1
%patch -P117 -p1

%build
%{__aclocal} -I config-scripts
%{__autoconf}
%configure \
	--enable-acl \
	--enable-dbus \
	%{?debug:--enable-debug} \
	--enable-gssapi%{!?with_gssapi:=no} \
	--enable-libpaper \
	--enable-libusb \
	%{?with_lspp:--enable-lspp} \
	--enable-shared \
	%{?with_static_libs:--enable-static} \
	%{?with_tcp_wrappers:--enable-tcp-wrappers} \
	--with-cups-group=lp \
	--with-cups-user=lp \
	--with-system-groups=sys \
	--with-config-file-perm=0640 \
	--with-log-file-perm=0640 \
	--with-dbusdir=/etc/dbus-1 \
	--with-docdir=%{_ulibdir}/%{name}/cgi-bin \
	--with-pkgconfpath=%{_pkgconfigdir} \
	--with-printcap=/etc/printcap \
	--with-dnssd=%{?with_avahi:avahi}%{?with_dnssd:mdnsresponder}%{!?with_avahi:%{!?with_dnssd:no}} \
	--with-optim=-Wno-format-y2k \
	%{?with_systemd:--with-systemd=%{systemdunitdir}} \
	--with-ondemand=%{?with_systemd:systemd}%{!?with_systemd:no} \
	--with-tls=%{?with_gnutls:gnutls}%{!?with_gnutls:openssl}

%{__make} %{?debug:OPTIONS="-DDEBUG"}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,logrotate.d,modprobe.d,security,sysconfig/rc-inetd} \
	$RPM_BUILD_ROOT/var/run/cups \
	$RPM_BUILD_ROOT/var/log/{,archive/}cups \
	$RPM_BUILD_ROOT{%{systemdunitdir},%{systemdtmpfilesdir}}

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT \
	CUPS_USER=$(id -u) \
	CUPS_GROUP=$(id -g)

%if %{with avahi}
ln -s %{_ulibdir}/cups/backend/dnssd $RPM_BUILD_ROOT%{_ulibdir}/cups/backend/mdns
%endif

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
cp -pf %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/%{name}
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/cups/mailto.conf
sed -e 's|__ULIBDIR__|%{_ulibdir}|g' %{SOURCE5} > $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cups-lpd
cp -p %{SOURCE6} $RPM_BUILD_ROOT/etc/modprobe.d/cups.conf
cp -p %{SOURCE7} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

touch $RPM_BUILD_ROOT/var/log/cups/{access_log,error_log,page_log}
touch $RPM_BUILD_ROOT/etc/security/blacklist.cups
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{classes,printers}.conf

cat >$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/client.conf <<'EOF'
# Encryption Always
# ServerName enter.server.IP.or.name
EOF

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Deal with config migration due to CVE-2012-5519 (STR #4223)
_keywords="^\(AccessLog\|CacheDir\|ConfigFilePerm\|\
DataDir\|DocumentRoot\|ErrorLog\|FatalErrors\|\
FileDevice\|FontPath\|Group\|LogFilePerm\|\
LPDConfigFile\|PageLog\|Printcap\|PrintcapFormat\|\
RemoteRoot\|RequestRoot\|ServerBin\|ServerCertificate\|\
ServerKey\|ServerRoot\|SMBConfigFile\|StateDir\|\
SystemGroup\|SystemGroupAuthKey\|TempDir\|User\)\b"
if [ -f %{_sysconfdir}/cups/cupsd.conf ] && grep -iq "$_keywords" %{_sysconfdir}/cups/cupsd.conf; then
	echo "# Settings automatically moved from cupsd.conf by RPM package:" >> %{_sysconfdir}/cups/cups-files.conf
	grep -i "$_keywords" %{_sysconfdir}/cups/cupsd.conf >> %{_sysconfdir}/cups/cups-files.conf || :
	%{__sed} -i -e "s,$_keywords,#&,ig" %{_sysconfdir}/cups/cupsd.conf || :
fi
/sbin/chkconfig --add cups
%service cups restart "cups daemon"
/sbin/rmmod usblp > /dev/null 2>&1 || :
%systemd_post cups.service cups.socket cups.path

%preun
if [ "$1" = "0" ]; then
	%service cups stop
	/sbin/chkconfig --del cups
fi
%systemd_preun cups.service cups.socket cups.path

%postun
%systemd_reload

%triggerpostun -- cups < 1:1.5.2-1
%systemd_trigger cups.service cups.socket cups.path

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig
%post	image-lib -p /sbin/ldconfig
%postun	image-lib -p /sbin/ldconfig

%post lpd
%service -q rc-inetd reload

%postun lpd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%doc *.md
%attr(640,root,root) %config %verify(not md5 mtime size) /etc/pam.d/cups
%attr(754,root,root) /etc/rc.d/init.d/cups
/etc/dbus-1/system.d/cups.conf
/etc/modprobe.d/cups.conf
%if %{with systemd}
%{systemdunitdir}/cups.service
%{systemdunitdir}/cups.socket
%{systemdunitdir}/cups.path
%{systemdunitdir}/system-cups.slice
%{systemdtmpfilesdir}/%{name}.conf
%endif
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/classes.conf
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/cups-files.conf
%attr(640,root,lp) %{_sysconfdir}/%{name}/cups-files.conf.default
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/cupsd.conf
%attr(640,root,lp) %{_sysconfdir}/%{name}/cupsd.conf.default
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/printers.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/mailto.conf
%attr(600,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/snmp.conf
%attr(640,root,lp) %{_sysconfdir}/%{name}/snmp.conf.default
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.cups
%dir %attr(700,root,lp) %{_sysconfdir}/%{name}/ssl
%dir %attr(755,root,lp) %{_sysconfdir}/%{name}/ppd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}
%attr(755,root,root) %{_bindir}/cupstestppd
%attr(755,root,root) %{_bindir}/ippeveprinter
%attr(755,root,root) %{_sbindir}/cupsctl
%attr(755,root,root) %{_sbindir}/cupsd
%attr(755,root,root) %{_sbindir}/cupsfilter

%dir %{_ulibdir}/cups
%dir %{_ulibdir}/cups/backend
%if %{with avahi}
%attr(755,root,root) %{_ulibdir}/cups/backend/dnssd
%attr(755,root,root) %{_ulibdir}/cups/backend/mdns
%endif
%attr(755,root,root) %{_ulibdir}/cups/backend/http
%attr(755,root,root) %{_ulibdir}/cups/backend/https
%attr(755,root,root) %{_ulibdir}/cups/backend/ipp
%attr(755,root,root) %{_ulibdir}/cups/backend/ipps
%attr(755,root,root) %{_ulibdir}/cups/backend/lpd
%attr(755,root,root) %{_ulibdir}/cups/backend/snmp
%attr(755,root,root) %{_ulibdir}/cups/backend/socket

%dir %{_ulibdir}/cups/cgi-bin
%{_ulibdir}/cups/cgi-bin/help
%{_ulibdir}/cups/cgi-bin/images
%attr(755,root,root) %{_ulibdir}/cups/cgi-bin/*.cgi
%{_ulibdir}/cups/cgi-bin/*.css
%{_ulibdir}/cups/cgi-bin/*.html
%{_ulibdir}/cups/cgi-bin/*.png
%{_ulibdir}/cups/cgi-bin/*.txt
%lang(da) %{_ulibdir}/cups/cgi-bin/da
%lang(de) %{_ulibdir}/cups/cgi-bin/de
%lang(es) %{_ulibdir}/cups/cgi-bin/es
%lang(fr) %{_ulibdir}/cups/cgi-bin/fr
%lang(ja) %{_ulibdir}/cups/cgi-bin/ja
%lang(pt_BR) %{_ulibdir}/cups/cgi-bin/pt_BR
%lang(ru) %{_ulibdir}/cups/cgi-bin/ru

%dir %{_ulibdir}/cups/command
%attr(755,root,root) %{_ulibdir}/cups/command/ippevepcl
%attr(755,root,root) %{_ulibdir}/cups/command/ippeveps
%dir %{_ulibdir}/cups/daemon
%attr(755,root,root) %{_ulibdir}/cups/daemon/cups-deviced
%attr(755,root,root) %{_ulibdir}/cups/daemon/cups-driverd
%attr(755,root,root) %{_ulibdir}/cups/daemon/cups-exec
%dir %{_ulibdir}/cups/driver
%dir %{_ulibdir}/cups/filter
%attr(755,root,root) %{_ulibdir}/cups/filter/commandtops
%attr(755,root,root) %{_ulibdir}/cups/filter/gziptoany
%attr(755,root,root) %{_ulibdir}/cups/filter/pstops
%attr(755,root,root) %{_ulibdir}/cups/filter/rastertoepson
%attr(755,root,root) %{_ulibdir}/cups/filter/rastertohp
%attr(755,root,root) %{_ulibdir}/cups/filter/rastertolabel
%attr(755,root,root) %{_ulibdir}/cups/filter/rastertopwg
%dir %{_ulibdir}/cups/monitor
%attr(755,root,root) %{_ulibdir}/cups/monitor/bcp
%attr(755,root,root) %{_ulibdir}/cups/monitor/tbcp
%dir %{_ulibdir}/cups/notifier
%attr(755,root,root) %{_ulibdir}/cups/notifier/dbus
%attr(755,root,root) %{_ulibdir}/cups/notifier/mailto
%attr(755,root,root) %{_ulibdir}/cups/notifier/rss

%dir %{_datadir}/cups/drivers
%dir %{_datadir}/cups/mime
%{_datadir}/cups/mime/mime.convs
%{_datadir}/cups/mime/mime.types
%dir %{_datadir}/cups/model
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
%lang(da) %{_datadir}/cups/templates/da
%lang(de) %{_datadir}/cups/templates/de
%lang(es) %{_datadir}/cups/templates/es
%lang(fr) %{_datadir}/cups/templates/fr
%lang(ja) %{_datadir}/cups/templates/ja
%lang(pt_BR) %{_datadir}/cups/templates/pt_BR
%lang(ru) %{_datadir}/cups/templates/ru
%{_mandir}/man1/cups.1*
%{_mandir}/man1/cupstestppd.1*
%{_mandir}/man1/ippeveprinter.1*
%{_mandir}/man5/classes.conf.5*
%{_mandir}/man5/cups-files.conf.5*
%{_mandir}/man5/cups-snmp.conf.5*
%{_mandir}/man5/cupsd.conf.5*
%{_mandir}/man5/cupsd-logs.5*
%{_mandir}/man5/ipptoolfile.5*
%{_mandir}/man5/mailto.conf.5*
%{_mandir}/man5/mime.convs.5*
%{_mandir}/man5/mime.types.5*
%{_mandir}/man5/printers.conf.5*
%{_mandir}/man5/subscriptions.conf.5*
%{_mandir}/man7/backend.7*
%{_mandir}/man7/filter.7*
%{_mandir}/man7/ippevepcl.7*
%{_mandir}/man7/ippeveps.7*
%{_mandir}/man7/notifier.7*
%{_mandir}/man8/cups-deviced.8*
%{_mandir}/man8/cups-driverd.8*
%{_mandir}/man8/cups-exec.8*
%{_mandir}/man8/cups-snmp.8*
%{_mandir}/man8/cupsctl.8*
%{_mandir}/man8/cupsd.8*
%{_mandir}/man8/cupsd-helper.8*
%{_mandir}/man8/cupsfilter.8*

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

%files backend-usb
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/cups/backend/usb
%dir %{_datadir}/cups/usb
%{_datadir}/cups/usb/org.cups.usb-quirks

%files lpd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/cups-lpd
%attr(755,root,root) %{_ulibdir}/cups/daemon/cups-lpd
%if %{with systemd}
%{systemdunitdir}/cups-lpd.socket
%{systemdunitdir}/cups-lpd@.service
%endif
%{_mandir}/man8/cups-lpd.8*

%files ppdc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppd*
%dir %{_datadir}/cups/drv
%{_datadir}/cups/drv/sample.drv
%dir %{_datadir}/cups/examples
%{_datadir}/cups/examples/*.drv
%dir %{_datadir}/cups/ppdc
%{_datadir}/cups/ppdc/epson.h
%{_datadir}/cups/ppdc/hp.h
%{_datadir}/cups/ppdc/label.h
%{_datadir}/cups/ppdc/font.defs
%{_datadir}/cups/ppdc/media.defs
%{_datadir}/cups/ppdc/raster.defs
%{_mandir}/man1/ppd*.1*
%{_mandir}/man5/ppdcfile.5*

%files clients
%defattr(644,root,root,755)
%attr(644,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/client.conf
%attr(755,root,root) %{_bindir}/cancel
%{?with_avahi:%attr(755,root,root) %{_bindir}/ippfind}
%attr(755,root,root) %{_bindir}/ipptool
%attr(755,root,root) %{_bindir}/lp
%attr(755,root,root) %{_bindir}/lpoptions
%attr(755,root,root) %{_bindir}/lpq
%attr(755,root,root) %{_bindir}/lpr
%attr(755,root,root) %{_bindir}/lprm
%attr(755,root,root) %{_bindir}/lpstat
%attr(755,root,root) %{_sbindir}/cupsaccept
%attr(755,root,root) %{_sbindir}/cupsenable
%attr(755,root,root) %{_sbindir}/cupsdisable
%attr(755,root,root) %{_sbindir}/cupsreject
%attr(755,root,root) %{_sbindir}/disable
%attr(755,root,root) %{_sbindir}/enable
%attr(755,root,root) %{_sbindir}/lpadmin
%attr(755,root,root) %{_sbindir}/lpc
%attr(755,root,root) %{_sbindir}/lpinfo
%attr(755,root,root) %{_sbindir}/lpmove
%{_datadir}/cups/ipptool
%{_desktopdir}/cups.desktop
%{_iconsdir}/hicolor/*/apps/cups.png
%{_mandir}/man1/cancel.1*
%{?with_avahi:%{_mandir}/man1/ippfind.1*}
%{_mandir}/man1/ipptool.1*
%{_mandir}/man1/lp.1*
%{_mandir}/man1/lpoptions.1*
%{_mandir}/man1/lpq.1*
%{_mandir}/man1/lpr.1*
%{_mandir}/man1/lprm.1*
%{_mandir}/man1/lpstat.1*
%{_mandir}/man5/client.conf.5*
%{_mandir}/man8/cupsaccept.8*
%{_mandir}/man8/cupsenable.8*
%{_mandir}/man8/cupsdisable.8*
%{_mandir}/man8/cupsreject.8*
%{_mandir}/man8/lpadmin.8*
%{_mandir}/man8/lpc.8*
%{_mandir}/man8/lpinfo.8*
%{_mandir}/man8/lpmove.8*

%files lib
%defattr(644,root,root,755)
%dir %attr(755,root,lp) %{_sysconfdir}/%{name}
%attr(755,root,root) %{_libdir}/libcups.so.2
%dir %{_datadir}/cups
%lang(ca) %{_localedir}/ca/cups_ca.po
%lang(cs) %{_localedir}/cs/cups_cs.po
%lang(da) %{_localedir}/da/cups_da.po
%lang(de) %{_localedir}/de/cups_de.po
%{_localedir}/en/cups_en.po
%lang(es) %{_localedir}/es/cups_es.po
%lang(fr) %{_localedir}/fr/cups_fr.po
%lang(it) %{_localedir}/it/cups_it.po
%lang(ja) %{_localedir}/ja/cups_ja.po
%lang(pt_BR) %{_localedir}/pt_BR/cups_pt_BR.po
%lang(ru) %{_localedir}/ru/cups_ru.po
%lang(zh_CN) %{_localedir}/zh_CN/cups_zh_CN.po

%files image-lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcupsimage.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cups-config
%attr(755,root,root) %{_libdir}/libcups.so
%attr(755,root,root) %{_libdir}/libcupsimage.so
%{_includedir}/cups
%{_pkgconfigdir}/cups.pc
%{_mandir}/man1/cups-config.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcups.a
%{_libdir}/libcupsimage.a
%endif
