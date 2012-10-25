%define	snap	20121025
Summary:	A set of CUPS printer drivers for SPL (Samsung Printer Language) printers
Summary(hu.UTF-8):	CUPS meghajtók sokasága SPL (Samsung Printer Language) nyomtatókhoz
Summary(pl.UTF-8):	Zestaw sterowników do drukarek obsługujących SPL (Samsung Printer Language)
Name:		cups-driver-splix
Version:	2.0.0
Release:	11.%{snap}.3
License:	GPL
Group:		Applications
# Source0:	http://downloads.sourceforge.net/splix/splix-%{version}.tar.bz2
Source0:	splix-%{snap}.tar.bz2
# Source0-md5:	1681508ba874da1a57dfaef28e15a9b8
Source1:	http://splix.ap2c.org/samsung_cms.tar.bz2
# Source1-md5:	51bf60a93575eb392ed6ad5d43e00e36
URL:		http://splix.sourceforge.net/
BuildRequires:	cups-devel
BuildRequires:	jbigkit-devel
BuildRequires:	libstdc++-devel
Requires:	cups
Requires:	cups-clients
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_datadir	%(cups-config --datadir 2>/dev/null)
%define 	_libdir		%(cups-config --serverbin 2>/dev/null)
%define		_cupsppddir	%{_datadir}/model
%define 	_cupsfilterdir	%{_libdir}/filter
%define 	_cupsfontsdir	%{_datadir}/fonts
%define		_cupsprofilesdir	%{_datadir}/profiles

%description
Splix is a driver for printers that speak SPL (Samsung Printer
Language). This includes printers made by Samsung and several Xerox
printers.

%description -l hu.UTF-8
A splix meghajtókat tartalmaz SPL (Samsung Printer Language)
nyomtatókhoz. Ezek a Samsung által gyártott nyomtatók és még néhány a
Xerox termékei közül.

%description -l pl.UTF-8
Splix jest sterownikiem do drukarek obsługującym SPL (Samsung Printer
Language). Wspiera modele wyprodukowane przez Samsunga jak również
niektóre drukarki Xeroksa.

%package samsung
Summary:	Splix Samsung drivers to CUPS
Summary(hu.UTF-8):	Splix Samsung meghajtók CUPS-hoz
Summary(pl.UTF-8):	Splix sterownik Samsunga do CUPS
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description samsung
Splix Samsung drivers to CUPS

%description samsung -l hu.UTF-8
Splix Samsung meghajtók CUPS-hoz.

%description samsung -l pl.UTF-8
Splix sterownik Samsunga do CUPS

%package xerox
Summary:	Splix Xerox drivers to CUPS
Summary(hu.UTF-8):	Splix Xerox meghajtók CUPS-hoz
Summary(pl.UTF-8):	Splix sterownik Xeroksa do CUPS
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description xerox
Splix Xerox drivers to CUPS

%description xerox -l hu.UTF-8
Splix Xerox meghajtók CUPS-hoz.

%description xerox -l pl.UTF-8
Splix sterownik Xeroksa do CUPS

%package dell
Summary:	Splix Dell drivers to CUPS
Summary(hu.UTF-8):	Splix Dell meghajtók CUPS-hoz
Summary(pl.UTF-8):	Splix sterownik Della do CUPS
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description dell
Splix Dell drivers to CUPS

%description dell -l hu.UTF-8
Splix Dell meghajtók CUPS-hoz.

%description dell -l pl.UTF-8
Splix sterownik Della do CUPS

%package lexmark
Summary:	Splix Lexmark drivers to CUPS
Summary(hu.UTF-8):	Splix Lexmark meghajtók CUPS-hoz
Summary(pl.UTF-8):	Splix sterownik Lexmark do CUPS
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description lexmark
Splix Lexmark drivers to CUPS

%description dell -l hu.UTF-8
Splix Lexmark meghajtók CUPS-hoz.

%description dell -l pl.UTF-8
Splix sterownik Lexmark do CUPS

%package toshiba
Summary:	Splix Toshiba drivers to CUPS
Summary(hu.UTF-8):	Splix Toshiba meghajtók CUPS-hoz
Summary(pl.UTF-8):	Splix sterownik Toshiba do CUPS
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description toshiba
Splix Toshiba drivers to CUPS

%description toshiba -l hu.UTF-8
Splix Toshiba meghajtók CUPS-hoz.

%description toshiba -l pl.UTF-8
Splix sterownik Toshiba do CUPS

%prep
%setup -q -n splix -a1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTCXXFLAGS="%{rpmcxxflags}" \
	OPTLDFLAGS="%{rpmldflags} %{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_cupsprofilesdir}/samsung

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CUPSFILTER=%{_cupsfilterdir}

cp -a cms/* $RPM_BUILD_ROOT%{_cupsprofilesdir}/samsung


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README THANKS TODO
%attr(755,root,root) %{_cupsfilterdir}/rastertoqpdl
%attr(755,root,root) %{_cupsfilterdir}/pstoqpdl

%files samsung
%defattr(644,root,root,755)
%{_cupsppddir}/samsung
%dir %{_cupsprofilesdir}
%{_cupsprofilesdir}/samsung

%files xerox
%defattr(644,root,root,755)
%{_cupsppddir}/xerox

%files dell
%defattr(644,root,root,755)
%{_cupsppddir}/dell

%files lexmark
%defattr(644,root,root,755)
%{_cupsppddir}/lexmark

%files toshiba
%defattr(644,root,root,755)
%{_cupsppddir}/toshiba
