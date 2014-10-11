Summary:	DTS Coherent Acoustics decoder
Name:		libdca
Version:	0.0.5
Release:	5
License:	GPL
Group:		Libraries
Source0:	http://download.videolan.org/pub/videolan/libdca/0.0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	dab6b2795c66a82a6fcd4f8343343021
URL:		http://www.videolan.org/libdca.html
Patch0:		%{name}-opt.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free decoder for the DTS Coherent Acoustics format. It consists of a
library and a command line decoder. DTS is a high quality
multi-channel (5.1) digital audio format used in DVDs and DTS audio
CDs.

%package devel
Summary:	Header files for libdca library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdca library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

