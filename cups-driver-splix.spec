Summary:	A set of CUPS printer drivers for SPL (Samsung Printer Language) printers
Summary(hu.UTF-8):	CUPS meghajtók sokasága SPL (Samsung Printer Language) nyomtatókhoz
Summary(pl.UTF-8):	Zestaw sterowników do drukarek obsługujących SPL (Samsung Printer Language)
Name:		cups-driver-splix
Version:	2.0.1
Release:	1
License:	GPL v2
Group:		Applications/Printing
#Source0Download: https://github.com/OpenPrinting/splix/releases
Source0:	https://github.com/OpenPrinting/splix/releases/download/%{version}/splix-%{version}.tar.xz
# Source0-md5:	99a15ec82054ef4016fcaac07978ecc6
# from http://splix.ap2c.org/samsung_cms.tar.bz2, no longer available
Source1:	samsung_cms.tar.bz2
# Source1-md5:	51bf60a93575eb392ed6ad5d43e00e36
URL:		https://openprinting.github.io/splix/
BuildRequires:	cups-devel
BuildRequires:	jbigkit-devel
BuildRequires:	libstdc++-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cups
Requires:	cups-clients
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	cups_datadir		%(cups-config --datadir 2>/dev/null)
%define 	cups_serverbindir	%(cups-config --serverbin 2>/dev/null)

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

%package dell
Summary:	Splix Dell drivers for CUPS
Summary(hu.UTF-8):	Splix Dell meghajtók CUPS-hoz
Summary(pl.UTF-8):	Sterownik Splix do CUPS-a dla drukarek firmy Dell
Group:		Applications/Printing
Requires:	%{name} = %{version}-%{release}

%description dell
Splix Dell drivers for CUPS.

%description dell -l hu.UTF-8
Splix Dell meghajtók CUPS-hoz.

%description dell -l pl.UTF-8
Sterownik Splix do CUPS-a dla drukarek firmy Dell.

%package lexmark
Summary:	Splix Lexmark drivers for CUPS
Summary(hu.UTF-8):	Splix Lexmark meghajtók CUPS-hoz
Summary(pl.UTF-8):	Sterownik Splix do CUPS-a dla drukarek firmy Lexmark
Group:		Applications/Printing
Requires:	%{name} = %{version}-%{release}

%description lexmark
Splix Lexmark drivers for CUPS.

%description lexmark -l hu.UTF-8
Splix Lexmark meghajtók CUPS-hoz.

%description lexmark -l pl.UTF-8
Sterownik Splix do CUPS-a dla drukarek firmy Lexmark.

%package samsung
Summary:	Splix Samsung drivers for CUPS
Summary(hu.UTF-8):	Splix Samsung meghajtók CUPS-hoz
Summary(pl.UTF-8):	Sterownik Splix do CUPS-a dla drukarek firmy Samsung
Group:		Applications/Printing
Requires:	%{name} = %{version}-%{release}

%description samsung
Splix Samsung drivers for CUPS

%description samsung -l hu.UTF-8
Splix Samsung meghajtók CUPS-hoz.

%description samsung -l pl.UTF-8
Sterownik Splix do CUPS-a dla drukarek firmy Samsung.

%package toshiba
Summary:	Splix Toshiba drivers for CUPS
Summary(hu.UTF-8):	Splix Toshiba meghajtók CUPS-hoz
Summary(pl.UTF-8):	Sterownik Splix do CUPS-a dla drukarek firmy Toshiba
Group:		Applications/Printing
Requires:	%{name} = %{version}-%{release}

%description toshiba
Splix Toshiba drivers for CUPS.

%description toshiba -l hu.UTF-8
Splix Toshiba meghajtók CUPS-hoz.

%description toshiba -l pl.UTF-8
Sterownik Splix do CUPS-a dla drukarek firmy Toshiba.

%package xerox
Summary:	Splix Xerox drivers for CUPS
Summary(hu.UTF-8):	Splix Xerox meghajtók CUPS-hoz
Summary(pl.UTF-8):	Sterownik Splix do CUPS-a dla drukarek firmy Xerox
Group:		Applications/Printing
Requires:	%{name} = %{version}-%{release}

%description xerox
Splix Xerox drivers for CUPS.

%description xerox -l hu.UTF-8
Splix Xerox meghajtók CUPS-hoz.

%description xerox -l pl.UTF-8
Sterownik Splix do CUPS-a dla drukarek firmy Xerox.

%prep
%setup -q -n splix-%{version} -a1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTIM_CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags} %{rpmcxxflags}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{cups_datadir}/profiles/samsung

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CUPSFILTER=%{cups_serverbindir}/filter

cp -a cms/* $RPM_BUILD_ROOT%{cups_datadir}/profiles/samsung


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README.md THANKS TODO
%attr(755,root,root) %{cups_serverbindir}/filter/rastertoqpdl
%attr(755,root,root) %{cups_serverbindir}/filter/pstoqpdl

%files dell
%defattr(644,root,root,755)
%{cups_datadir}/model/dell

%files lexmark
%defattr(644,root,root,755)
%{cups_datadir}/model/lexmark

%files samsung
%defattr(644,root,root,755)
%{cups_datadir}/model/samsung
%dir %{cups_datadir}/profiles
%{cups_datadir}/profiles/samsung

%files toshiba
%defattr(644,root,root,755)
%{cups_datadir}/model/toshiba

%files xerox
%defattr(644,root,root,755)
%{cups_datadir}/model/xerox
