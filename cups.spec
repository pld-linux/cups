Summary:	Common Unix Printing System	
Name:		cups
Version:	1.1.2
Release:	1
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

%prep
%setup -q
%patch -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make}    prefix=$RPM_BUILD_ROOT \
exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
        BINDIR=$RPM_BUILD_ROOT%{_bindir} \
        DATADIR=$RPM_BUILD_ROOT%{_datadir}/cups \
        DOCDIR=$RPM_BUILD_ROOT%{_datadir}/doc/cups \
        INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
        LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
        LOCALEDIR=$RPM_BUILD_ROOT%{_datadir}/locale \
MANDIR=$RPM_BUILD_ROOT%{_prefix}/man \
        PAMDIR=$RPM_BUILD_ROOT/etc/pam.d \
        REQUESTS=$RPM_BUILD_ROOT/var/spool/cups \
SBINDIR=$RPM_BUILD_ROOT%{_sbindir} \
        SERVERBIN=$RPM_BUILD_ROOT%{_libdir}/cups \
SERVERROOT=$RPM_BUILD_ROOT%{_sysconfdir}/cups \
        install 


%clean

%files 
%defattr(644,root,root,755)
