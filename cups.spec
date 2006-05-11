#
# Conditional build:
%bcond_without	php	# don't build PHP extension
%bcond_without	perl	# don't build Perl extension
#
# TODO:
# - build/install java ext ?
# - perl BRs
%include	/usr/lib/rpm/macros.perl
%define		pdir CUPS
Summary:	Common Unix Printing System
Summary(pl):	Popularny system druku dla Uniksa
Summary(pt_BR):	Sistema Unix de Impressão
Name:		cups
Version:	1.2.0
Release:	0.1
Epoch:		1
License:	GPL/LGPL
Group:		Applications/Printing
Source0:	http://ftp.easysw.com/pub/cups/%{version}/%{name}-%{version}-source.tar.bz2
# Source0-md5:	a168b0b1c8bb946060e659e1df2927c5
Source1:	%{name}.init
Source2:	%{name}.pamd
Source3:	%{name}.logrotate
Patch0:		%{name}-config.patch
Patch1:		%{name}-lp-lpr.patch
Patch2:		%{name}-options.patch
Patch3:		%{name}-ENCRYPTIONtxt.patch
Patch4:		%{name}-man_pages_linking.patch
Patch5:		%{name}-nolibs.patch
Patch6:		%{name}-nostrip.patch
Patch7:		%{name}-rpath.patch
Patch8:		%{name}-gcc34.patch
Patch9:		%{name}-tmpdir.patch
Patch10:	%{name}-gcc4.patch
Patch11:	%{name}-CAN-2005-2097.patch
Patch12:	%{name}-anonymous_jobs.patch
URL:		http://www.cups.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	openslp-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
%{?with_php:BuildRequires:	php-devel >= 4:5.0.0}
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.77.3
Requires:	rc-scripts
Obsoletes:	LPRng
Obsoletes:	lpr
Conflicts:	ghostscript < 7.05.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%if %{with php}
%define		_php_configdir /etc/php
%define		_php_extensiondir %(php-config --extension-dir)
%endif

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

%description -l pl
CUPS dostarcza standardowy poziom drukowania dla systemów uniksowych.
CUPS u¿ywa protoko³u IPP - Internet Printint Protocol jako podstawy do
zarz±dzania zadaniami i kolejkami druku.

%description -l pt_BR
O sistema Unix de impressão (CUPS) fornece uma camada de impressão
portável para os sistemas operacionais baseados no UNIX®.

%package lib
Summary:	Common Unix Printing System Libraries
Summary(pl):	Biblioteki dla CUPS
Summary(pt_BR):	Sistema Unix de Impressão - bibliotecas para uso em clientes cups
Group:		Libraries
Provides:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	cups-libs
Obsoletes:	libcups1

%description lib
Common Unix Printing System Libraries.

%description lib -l pl
Biblioteki dla CUPS.

%description lib -l pt_BR
Bibliotecas CUPS requeridas pelos clientes CUPS.

%package clients
Summary:	Common Unix Printing System Clients
Summary(pl):	Aplikacje klienckie dla CUPS
Group:		Applications/Printing
Provides:	%{name}-clients = %{epoch}:%{version}-%{release}
Conflicts:	LPRng

%description clients
Common Unix Printing System Clients.

%description clients -l pl
Aplikacje klienckie dla CUPS.

%package image-lib
Summary:	Common Unix Printing System Libraries - images manipulation
Summary(pl):	Biblioteki dla CUPS - obs³uga formatów graficznych
Summary(pt_BR):	Sistema Unix de Impressão - bibliotecas para uso em clientes cups
Group:		Libraries
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Obsoletes:	libcups1

%description image-lib
Common Unix Printing System Libraries - images manupalation.

%description image-lib -l pl
Biblioteki dla CUPS - obs³uga formatów graficznych.

%description image-lib -l pt_BR
Bibliotecas CUPS requeridas pelos clientes CUPS.

%package devel
Summary:	Common Unix Printing System development files
Summary(pl):	Popularny System Druku dla Uniksa, pliki nag³ówkowe
Summary(pt_BR):	Sistema Unix de Impressão - ambiente de desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-image-lib = %{epoch}:%{version}-%{release}
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Obsoletes:	libcups1-devel

%description devel
Common Unix Printing System development files.

%description devel -l pl
Popularny System Druku dla Uniksa, pliki nag³ówkowe.

%description devel -l pt_BR
Este pacote é um adicional que contem um ambiente de desenvolvimento
para a criação de suporte a novas impressoras e novos serviços ao
CUPS.

%package static
Summary:	Common Unix Printing System static libraries
Summary(pl):	Popularny System Druku dla Uniksa, biblioteki statyczne
Summary(pt_BR):	Common Unix Printing System - bibliotecas estáticas
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Common Unix Printing System static libraries.

%description static -l pl
Popularny System Druku dla Uniksa, biblioteki statyczne.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de programas que usam as
bibliotecas do CUPS.

%package -n perl-cups
Summary:	Perl module for CUPS
Summary(pl):	Modu³ Perla CUPS
Group:		Development/Languages/Perl
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}

%description -n perl-cups
Perl module for Common Unix Printing System.

%description -n perl-cups -l pl
Modu³ Perla do Popularnego Systemu Druku dla Uniksa.

%package -n php-cups
Summary:	PHP module for CUPS
Summary(pl):	Modu³ PHP CUPS
Group:		Development/Languages/PHP
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
Requires:	php-common >= 4:5.0.0

%description -n php-cups
PHP module for Common Unix Printing System.

%description -n php-cups -l pl
Modu³ PHP do Popularnego Systemu Druku dla Uniksa.

%package backend-usb
Summary:	USB backend for CUPS
Summary(pl):	Backend USB dla CUPS-a
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-usb
This package allow CUPS printing on USB printers.

%description backend-usb -l pl
Ten pakiet umo¿liwia drukowanie z poziomu CUPS-a na drukarkach USB.

%package backend-serial
Summary:	Serial port backend for CUPS
Summary(pl):	Backend obs³uguj±cy porty szeregowe dla CUPS-a
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-serial
This package allow CUPS printing on printers connected by serial
ports.

%description backend-serial -l pl
Ten pakiet umo¿liwia drukowanie z poziomu CUPS-a na drukarkach
pod³±czonych do portów szeregowych.

%package backend-parallel
Summary:	Parallel port backend for CUPS
Summary(pl):	Backend obs³uguj±cy porty równoleg³e dla CUPS-a
Group:		Applications/Printing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description backend-parallel
This package allow CUPS printing on printers connected by parallel
ports.

%description backend-parallel -l pl
Ten pakiet umo¿liwia drukowanie z poziomu CUPS-a na drukarkach
pod³±czonych do portów równoleg³ych.

%prep
%setup -q
#patch0 -p1 todo
%patch1 -p1
%patch2 -p1
#patch3 -p1 obsoleted
%patch4 -p1
#patch5 -p1 to check
#patch6 -p1 to check
%patch7 -p1
#patch8 -p1 to check
# wtf?
#%patch9 -p1
#patch10 -p1 to check
#patch11 -p1 obsoleted
#patch12 -p1 to check

%build
%{__aclocal}
%{__autoconf}
%configure \
	--libdir=%{_ulibdir} \
	--enable-dbus \
	%{?debug:--enable-debug} \
	--with-docdir=%{_ulibdir}/%{name}/cgi-bin
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
	$RPM_BUILD_ROOT/var/log/{,archiv/}cups

%{__make} install \
	BUILDROOT=$RPM_BUILD_ROOT \
	CUPS_USER=$(id -u) \
	CUPS_GROUP=$(id -g)

if [ "%{_lib}" != "lib" ] ; then
	install -d $RPM_BUILD_ROOT%{_libdir}
	mv $RPM_BUILD_ROOT%{_ulibdir}/*.so* $RPM_BUILD_ROOT%{_libdir}
	#mv $RPM_BUILD_ROOT%{_ulibdir}/*.a $RPM_BUILD_ROOT%{_libdir}
fi

%if %{with php}
install -d $RPM_BUILD_ROOT%{_php_configdir}/conf.d
%{__make} -C scripting/php install \
	PHPDIR="%{__php_extensiondir}"
install -d $RPM_BUILD_ROOT%{_php_configdir}/conf.d
cat > $RPM_BUILD_ROOT%{_php_configdir}/conf.d/phpcups.ini << EOF
; Enable phpcups extension module
extension=phpcups.so
EOF
%endif

%if %{with perl}
cd scripting/perl
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../..
%endif

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/pam.d/%{name}
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/logrotate.d/%{name}

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/%{name}/model/*.ppd

# for internal HTTP browser:
cp doc/*.html	$RPM_BUILD_ROOT%{_ulibdir}/%{name}/cgi-bin
cp doc/*.css	$RPM_BUILD_ROOT%{_ulibdir}/%{name}/cgi-bin
cp doc/images/*	$RPM_BUILD_ROOT%{_ulibdir}/%{name}/cgi-bin/images

touch $RPM_BUILD_ROOT/var/log/cups/{access_log,error_log,page_log}
touch $RPM_BUILD_ROOT/etc/security/blacklist.cups
touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{classes,printers}.conf

# windows drivers can be put there.
install -d $RPM_BUILD_ROOT%{_datadir}/cups/drivers

# post-strip can't work on readonly files
chmod u+w $RPM_BUILD_ROOT%{perl_vendorarch}/auto/CUPS/CUPS.so

# check-files cleanup
rm -rf $RPM_BUILD_ROOT%{_mandir}/{,es/,fr/}cat?
rm -rf $RPM_BUILD_ROOT/etc/{init.d,rc?.d}/*

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
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%postun -n php-cups
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
#%doc *.gz doc/*.html doc/*.css doc/images
%doc *.txt
%attr(640,root,root) %config %verify(not md5 mtime size) /etc/pam.d/*
%attr(754,root,root) /etc/rc.d/init.d/cups
/etc/dbus-1/system.d/cups.conf
%dir %{_sysconfdir}/%{name}
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/classes.conf
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/cupsd.conf
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/printers.conf
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.convs
%attr(640,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.types
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.cups
#%dir %{_sysconfdir}/%{name}/certs
%dir %{_sysconfdir}/%{name}/interfaces
%dir %{_sysconfdir}/%{name}/ppd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/%{name}
%attr(4755,lp,root) %{_bindir}/lppasswd
%attr(755,root,root) %{_bindir}/cupstestppd
%attr(755,root,root) %{_bindir}/cupstestdsc
#%attr(755,root,root) %{_bindir}/cupsdisable
#%attr(755,root,root) %{_bindir}/cupsenable
%dir %{_ulibdir}/cups
%dir %{_ulibdir}/cups/*
%attr(755,root,root) %{_ulibdir}/cups/*/*
%exclude %{_ulibdir}/cups/backend/usb
%exclude %{_ulibdir}/cups/backend/serial
%exclude %{_ulibdir}/cups/backend/parallel
%attr(755,root,root) %{_sbindir}/cupsd
%{_datadir}/cups
%{_mandir}/man7/backend.7*
%{_mandir}/man1/cupstestppd.1*
%{_mandir}/man1/cupstestdsc.1*
%{_mandir}/man7/filter.7*
%{_mandir}/man1/lppasswd.1*
%{_mandir}/man[58]/*
#%lang(fr) %{_mandir}/fr/man1/backend.1*
#%lang(fr) %{_mandir}/fr/man1/cupstestppd.1*
#%lang(fr) %{_mandir}/fr/man1/filter.1*
#%lang(fr) %{_mandir}/fr/man1/lppasswd.1*
#%lang(fr) %{_mandir}/fr/man[58]/*
#%lang(es) %{_mandir}/es/man1/backend.1*
#%lang(es) %{_mandir}/es/man1/cupstestppd.1*
#%lang(es) %{_mandir}/es/man1/filter.1*
#%lang(es) %{_mandir}/es/man1/lppasswd.1*
#%lang(es) %{_mandir}/es/man[58]/*
#%{_datadir}/locale/C/cups_C
#%lang(be) %{_datadir}/locale/be/cups_be
#%lang(cs) %{_datadir}/locale/cs/cups_cs
#%lang(de) %{_datadir}/locale/de/cups_de
#%{_datadir}/locale/en/cups_en
#%lang(en_US) %{_datadir}/locale/en_US/cups_en_US
%lang(es) %{_datadir}/locale/es/cups_es.po
%lang(ja) %{_datadir}/locale/ja/cups_ja.po
#%lang(fr) %{_datadir}/locale/fr/cups_fr
#%lang(he) %{_datadir}/locale/he/cups_he
#%lang(it) %{_datadir}/locale/it/cups_it
#%lang(ru) %{_datadir}/locale/ru_RU/cups_ru_RU
%lang(sv) %{_datadir}/locale/sv/cups_sv.po
#%lang(uk) %{_datadir}/locale/uk/cups_uk
#%lang(uk) %{_datadir}/locale/uk_UA/cups_uk_UA
#%lang(zh_CN) %{_datadir}/locale/zh_CN/cups_zh_CN
/var/spool/cups
%attr(750,root,logs) %dir /var/log/archiv/cups
%attr(750,root,logs) %dir /var/log/cups
%attr(640,root,logs) %ghost /var/log/cups/access_log
%attr(640,root,logs) %ghost /var/log/cups/error_log
%attr(640,root,logs) %ghost /var/log/cups/page_log

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcups.so.*

%files clients
%defattr(644,root,root,755)
#%attr(644,root,lp) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/client.conf
%attr(755,root,root) %{_bindir}/cancel
%attr(755,root,root) %{_bindir}/lp
%attr(755,root,root) %{_bindir}/lpoptions
%attr(755,root,root) %{_bindir}/lpq
%attr(755,root,root) %{_bindir}/lpr
%attr(755,root,root) %{_bindir}/lprm
%attr(755,root,root) %{_bindir}/lpstat
%attr(755,root,root) %{_sbindir}/accept
%attr(755,root,root) %{_sbindir}/cupsaddsmb
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
%{_includedir}/cups
%{_libdir}/lib*.so
%{_mandir}/man1/cups-config*
%{_mandir}/man3/*
#%lang(fr) %{_mandir}/fr/man1/cups-config*
#%lang(es) %{_mandir}/es/man1/cups-config*

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/*.a

%if %{with perl}
%files -n perl-cups
%defattr(644,root,root,755)
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/CUPS
%{perl_vendorarch}/auto/CUPS/*.bs
%{perl_vendorarch}/auto/CUPS/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/CUPS/*.so
%endif

%if %{with php}
%files -n php-cups
%defattr(644,root,root,755)
%attr(755,root,root) %(_php_extensiondir)/*
%config(noreplace) %verify(not md5 mtime size) %{_php_configdir}/conf.d/phpcups.ini
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
