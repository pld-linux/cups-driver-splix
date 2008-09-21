Summary:	A set of CUPS printer drivers for SPL (Samsung Printer Language) printers
Name:		cups-driver-splix
Version:	1.1.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/splix/splix-%{version}.tar.bz2
# Source0-md5:	13af25dd72aae68b39eaf557d62957a5
Patch0:		%{name}-optflags.patch
URL:		http://splix.sourceforge.net/
BuildRequires:	cups-devel
Requires:	cups
Requires:	cups-clients
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_datadir	%(cups-config --datadir 2>/dev/null)
%define 	_libdir		%(cups-config --serverbin 2>/dev/null)
%define		_cupsppddir	%{_datadir}/model
%define 	_cupsfilterdir	%{_libdir}/filter
%define 	_cupsfontsdir	%{_datadir}/fonts

%description
Splix is a driver for printers that speak SPL (Samsung Printer
Language). This includes printers made by Samsung and several Xerox
printers.

%package samsung
Summary:	Splix Samsung drivers to CUPS
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description samsung
Splix Samsung drivers to CUPS

%package xerox
Summary:	Splix Xerox drivers to CUPS
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description xerox
Splix Xerox drivers to CUPS

%package dell
Summary:	Splix Dell drivers to CUPS
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description dell
Splix Dell drivers to CUPS

%prep
%setup -q -n splix-%{version}
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTCXXFLAGS="%{rpmcxxflags}" \
	OPTLDFLAGS="%{rpmldflags} %{rpmcxxflags}" \
	DISABLE_JBIG=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_cupsfilterdir}
install src/rastertospl2 $RPM_BUILD_ROOT%{_cupsfilterdir}
## samsung drivers
install -d $RPM_BUILD_ROOT%{_cupsppddir}/samsung
cp -a ppd/{cl{p,x}*,ml*} $RPM_BUILD_ROOT%{_cupsppddir}/samsung
## xerox drivers
install -d $RPM_BUILD_ROOT%{_cupsppddir}/xerox
cp -a ppd/ph* $RPM_BUILD_ROOT%{_cupsppddir}/xerox
## dell drivers
install -d $RPM_BUILD_ROOT%{_cupsppddir}/dell
cp -a ppd/1100* $RPM_BUILD_ROOT%{_cupsppddir}/dell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README THANKS TODO
%attr(755,root,root) %{_cupsfilterdir}/rastertospl2

%files samsung
%defattr(644,root,root,755)
%dir %{_cupsppddir}/samsung
%{_cupsppddir}/samsung/*

%files xerox
%defattr(644,root,root,755)
%dir %{_cupsppddir}/xerox
%{_cupsppddir}/xerox/*

%files dell
%defattr(644,root,root,755)
%dir %{_cupsppddir}/dell
%{_cupsppddir}/dell/*
