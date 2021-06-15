Summary:	Reliable Internet Stream Transport (RIST)
Summary(pl.UTF-8):	Reliable Internet Stream Transport (RIST) - niezawodny internetowy protokół strumieniowy
Name:		librist
Version:	0.2.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://code.videolan.org/rist/librist/-/tags
Source0:	https://code.videolan.org/rist/librist/-/archive/v%{version}/librist-v%{version}.tar.bz2
# Source0-md5:	03b79beae3603bc050f5ea35ac676962
URL:		https://code.videolan.org/rist/librist
BuildRequires:	cjson-devel
BuildRequires:	meson >= 0.51.0
BuildRequires:	ninja >= 1.5
# disabled in sources (as of 0.2.1)
#BuildRequires:	lz4-devel
BuildRequires:	mbedtls-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that can be used to easily add the RIST protocol to your
application.

%description -l pl.UTF-8
Biblioteka, za pomocą której można łatwo dodać do swojej aplikacji
obsługę protokołu RIST.

%package devel
Summary:	Header files for RIST library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RIST
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cjson-devel
#Requires:	lz4-devel
Requires:	mbedtls-devel

%description devel
Header files for RIST library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RIST.

%package static
Summary:	Static RIST library
Summary(pl.UTF-8):	Statyczna biblioteka RIST
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static RIST library.

%description static -l pl.UTF-8
Statyczna biblioteka RIST.

%prep
%setup -q -n librist-v%{version}

%build
%meson build \
	-Dfallback_builtin=false

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md THANKS.md
%attr(755,root,root) %{_bindir}/rist2rist
%attr(755,root,root) %{_bindir}/ristreceiver
%attr(755,root,root) %{_bindir}/ristsender
%attr(755,root,root) %{_bindir}/ristsrppasswd
%attr(755,root,root) %{_libdir}/librist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librist.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librist.so
%{_includedir}/librist
%{_pkgconfigdir}/librist.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/librist.a
