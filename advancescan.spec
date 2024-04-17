# TODO: system expat? (contains modified expat 1.95.8)
Summary:	AdvanceSCAN ROMs Manager
Summary(pl.UTF-8):	AdvanceSCAN - zarządca ROM-ów
Name:		advancescan
Version:	1.18
Release:	2
License:	GPL v2+
Group:		Applications/File
#Source0Download: https://github.com/amadvance/advancescan/releases
Source0:	https://github.com/amadvance/advancescan/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	85d964fe0d34a5722ce923f7fbb8a115
Patch0:		%{name}-throw.patch
URL:		http://www.advancemame.it/scan-readme
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdvanceSCAN is a command line ROM manager for AdvanceMAME, AdvanceMESS
and any other MAME derivative.

%description -l pl.UTF-8
AdvanceSCAN to działający z linii poleceń zarządca obrazów ROM dla
emulatorów AdvanceMAME, AdvanceMESS i innych pochodnych MAME.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS HISTORY README
%attr(755,root,root) %{_bindir}/advdiff
%attr(755,root,root) %{_bindir}/advscan
%{_mandir}/man1/advdiff.1*
%{_mandir}/man1/advscan.1*
