# Copyright (c) 2008, 2009 David Sugar, Tycho Softworks.
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.

%define	major	8
%define	libname			%mklibname ucommon
%define	libusecure		%mklibname usecure
%define	libcommoncpp	%mklibname commoncpp
%define	devname			%mklibname ucommon -d

Summary:	Portable C++ framework for threads and sockets
Name:		ucommon
Version:	7.0.0
Release:	2
License:	LGPLv3+
Group:		Development/C++
URL:		https://www.gnu.org/software/commoncpp
Source0:	https://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz.sig

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	graphviz
#BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(gnutls)

%description
GNU uCommon C++ is a lightweight library to facilitate using C++ design
patterns even for very deeply embedded applications, such as for systems using
uClibc along with POSIX threading support. For this reason, uCommon disables
language features that consume memory or introduce runtime overhead. uCommon
introduces some design patterns from Objective-C, such as reference counted
objects, memory pools, and smart pointers.  uCommon introduces some new
concepts for handling of thread locking and synchronization.

#--------------------------------------------------------------------

%package bin
Summary:	ucommon system and support applications
Group:		Development/Other 

%description bin
This is a collection of command line tools that use various aspects of the
ucommon library.  Some may be needed to prepare files or for development of
applications.

%files bin
%doc AUTHORS README COPYRIGHT NEWS SUPPORT ChangeLog
%{_bindir}/args
%{_bindir}/car
%{_bindir}/keywait
%{_bindir}/scrub*
%{_bindir}/mdsum
%{_bindir}/pdetach
%{_bindir}/sockaddr
%{_bindir}/urlout
%{_bindir}/zerofill
%{_mandir}/man1/args.*
%{_mandir}/man1/car.*
%{_mandir}/man1/keywait.*
%{_mandir}/man1/pdetach.*
%{_mandir}/man1/scrub*.*
%{_mandir}/man1/mdsum.*
%{_mandir}/man1/sockaddr.*
%{_mandir}/man1/urlout.*
%{_mandir}/man1/zerofill.*

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	ucommon library
Group:		System/Libraries

%description -n %{libname}
Runtime library for ucommon.

%files -n %{libname}
%{_libdir}/libucommon.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libusecure}
Summary:	usecure library
Group:		System/Libraries

%description -n %{libusecure}
Runtime library for usecure.

%files -n %{libusecure}
%{_libdir}/libusecure.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libcommoncpp}
Summary:	commoncpp library
Group:		System/Libraries

%description -n %{libcommoncpp}
Runtime library for commoncpp.

%files -n %{libcommoncpp}
%{_libdir}/libcommoncpp.so.%{major}*

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for building uCommon applications
Group:		Development/C++
Requires:	%{libname} = %{version}
Requires:	%{libusecure} = %{version}
Requires:	%{libcommoncpp} = %{version}
%rename	%{name}-devel

%description -n %{devname}
This package provides header and support files needed for building
applications that use the uCommon library and frameworks

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/ucommon/
%{_includedir}/commoncpp/
%{_libdir}/pkgconfig/*.pc
%{_bindir}/ucommon-config
%{_bindir}/commoncpp-config
%{_mandir}/man1/ucommon-config.*
%{_mandir}/man1/commoncpp-config.*
%{_datadir}/ucommon/cmake

#--------------------------------------------------------------------

%package doc
Group: Books/Computer books
Summary: Generated class documentation for uCommon

%description doc
Generated class documentation for GNU uCommon library from header files, 
html browsable.

%files doc
%doc AUTHORS README COPYRIGHT NEWS SUPPORT ChangeLog
%doc doc/html

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%cmake \
	-G Ninja
%ninja_build
%ninja_build --target doc
#%%make doc

%install
%ninja_install
#cd build
#%%make DESTDIR=%{buildroot} INSTALL="install -p" install
#chmod 0755 %{buildroot}%{_bindir}/ucommon-config
#chmod 0755 %{buildroot}%{_bindir}/commoncpp-config
#mkdir -p %{buildroot}/%{_mandir}/man1
#install -m644 ../utils/*.1 -D %{buildroot}/%{_mandir}/man1
#install -m644 ../*.1 -D %{buildroot}/%{_mandir}/man1
#cp -r doc ..

