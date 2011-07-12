# Copyright (c) 2008, 2009 David Sugar, Tycho Softworks.
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.

Name: ucommon
Summary: Portable C++ framework for threads and sockets
Version: 5.0.4
Release: %mkrel 1
License: LGPLv3+
URL: http://www.gnu.org/software/commoncpp
Source0: ucommon-%{version}.tar.bz2
Patch0:  sockaddr_missing.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: doxygen graphviz openssl-devel cmake
Group: Development/C++
Summary: Runtime library for portable C++ threading and sockets

%description
GNU uCommon C++ is a lightweight library to facilitate using C++ design
patterns even for very deeply embedded applications, such as for systems using
uClibc along with POSIX threading support. For this reason, uCommon disables
language features that consume memory or introduce runtime overhead. uCommon
introduces some design patterns from Objective-C, such as reference counted
objects, memory pools, and smart pointers.  uCommon introduces some new
concepts for handling of thread locking and synchronization

%package bin
Requires: %{name} = %{version}-%{release}
Group: Development/Other 
Summary: ucommon system and support applications

%package devel
Requires: %{name} = %{version}-%{release}
Requires: %{name}-bin = %{version}-%{release}
Requires: openssl-devel
Requires: pkgconfig
Group: Development/C++
Summary: Headers for building uCommon applications

%package doc
Group: Books/Computer books
Summary: Generated class documentation for uCommon

%description bin
This is a collection of command line tools that use various aspects of the
ucommon library.  Some may be needed to prepare files or for development of
applications.

%description devel
This package provides header and support files needed for building
applications that use the uCommon library and frameworks

%description doc
Generated class documentation for GNU uCommon library from header files, 
html browsable.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .sockaddr

%build

%cmake
%{__make} 
%make doc

%install
%{__rm} -rf %{buildroot}
cd build
%{__make} DESTDIR=%{buildroot} INSTALL="install -p" install
%{__chmod} 0755 %{buildroot}%{_bindir}/ucommon-config
%{__chmod} 0755 %{buildroot}%{_bindir}/commoncpp-config
mkdir -p %{buildroot}/%{_mandir}/man1
install -m644 ../utils/*.1 -D %{buildroot}/%{_mandir}/man1
install -m644 ../*.1 -D %{buildroot}/%{_mandir}/man1
cp -r doc ..

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING COPYING.LESSER COPYRIGHT NEWS SUPPORT ChangeLog
%{_libdir}/libucommon.so.*
%{_libdir}/libusecure.so.*
%{_libdir}/libcommoncpp.so.*

%files bin
%defattr(-,root,root,-)
%{_bindir}/args
%{_bindir}/car
%{_bindir}/scrub
%{_bindir}/mdsum
%{_bindir}/sockaddr
%{_bindir}/zerofill
%{_mandir}/man1/args.*
%{_mandir}/man1/car.*
%{_mandir}/man1/scrub.*
%{_mandir}/man1/mdsum.*
%{_mandir}/man1/sockaddr.*
%{_mandir}/man1/zerofill.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/ucommon/
%{_includedir}/commoncpp/
%{_libdir}/pkgconfig/*.pc
%{_bindir}/ucommon-config
%{_bindir}/commoncpp-config
%{_mandir}/man1/ucommon-config.*
%{_mandir}/man1/commoncpp-config.*

%files doc
%defattr(-,root,root,-)
%doc doc/html

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

