#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libqalculate
Version  : 3.4.0
Release  : 5
URL      : https://github.com/Qalculate/libqalculate/releases/download/v3.4.0/libqalculate-3.4.0.tar.gz
Source0  : https://github.com/Qalculate/libqalculate/releases/download/v3.4.0/libqalculate-3.4.0.tar.gz
Summary  : libqalculate
Group    : Development/Tools
License  : GPL-2.0
Requires: libqalculate-bin = %{version}-%{release}
Requires: libqalculate-data = %{version}-%{release}
Requires: libqalculate-lib = %{version}-%{release}
Requires: libqalculate-license = %{version}-%{release}
Requires: libqalculate-locales = %{version}-%{release}
Requires: libqalculate-man = %{version}-%{release}
BuildRequires : gettext
BuildRequires : gmp-dev
BuildRequires : intltool
BuildRequires : mpfr-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : readline-dev

%description
Qalculate! library and CLI
Qalculate! is a multi-purpose cross-platform desktop calculator.
It is simple to use but provides power and versatility normally reserved for complicated math packages,
as well as useful tools for everyday needs (such as currency conversion and percent calculation).
Features include a large library of customizable functions, unit calculations and conversion,
symbolic calculations (including integrals and equations), arbitrary precision, interval arithmetic,
plotting, and a user-friendly interface (GTK+ and CLI).

%package bin
Summary: bin components for the libqalculate package.
Group: Binaries
Requires: libqalculate-data = %{version}-%{release}
Requires: libqalculate-license = %{version}-%{release}

%description bin
bin components for the libqalculate package.


%package data
Summary: data components for the libqalculate package.
Group: Data

%description data
data components for the libqalculate package.


%package dev
Summary: dev components for the libqalculate package.
Group: Development
Requires: libqalculate-lib = %{version}-%{release}
Requires: libqalculate-bin = %{version}-%{release}
Requires: libqalculate-data = %{version}-%{release}
Provides: libqalculate-devel = %{version}-%{release}
Requires: libqalculate = %{version}-%{release}

%description dev
dev components for the libqalculate package.


%package doc
Summary: doc components for the libqalculate package.
Group: Documentation
Requires: libqalculate-man = %{version}-%{release}

%description doc
doc components for the libqalculate package.


%package lib
Summary: lib components for the libqalculate package.
Group: Libraries
Requires: libqalculate-data = %{version}-%{release}
Requires: libqalculate-license = %{version}-%{release}

%description lib
lib components for the libqalculate package.


%package license
Summary: license components for the libqalculate package.
Group: Default

%description license
license components for the libqalculate package.


%package locales
Summary: locales components for the libqalculate package.
Group: Default

%description locales
locales components for the libqalculate package.


%package man
Summary: man components for the libqalculate package.
Group: Default

%description man
man components for the libqalculate package.


%prep
%setup -q -n libqalculate-3.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571461334
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1571461334
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libqalculate
cp %{_builddir}/libqalculate-3.4.0/COPYING %{buildroot}/usr/share/package-licenses/libqalculate/dfac199a7539a404407098a2541b9482279f690d
%make_install
%find_lang libqalculate

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qalc

%files data
%defattr(-,root,root,-)
/usr/share/qalculate/currencies.xml
/usr/share/qalculate/datasets.xml
/usr/share/qalculate/elements.xml
/usr/share/qalculate/eurofxref-daily.xml
/usr/share/qalculate/functions.xml
/usr/share/qalculate/planets.xml
/usr/share/qalculate/prefixes.xml
/usr/share/qalculate/units.xml
/usr/share/qalculate/variables.xml

%files dev
%defattr(-,root,root,-)
/usr/include/libqalculate/BuiltinFunctions.h
/usr/include/libqalculate/Calculator.h
/usr/include/libqalculate/DataSet.h
/usr/include/libqalculate/ExpressionItem.h
/usr/include/libqalculate/Function.h
/usr/include/libqalculate/MathStructure.h
/usr/include/libqalculate/Number.h
/usr/include/libqalculate/Prefix.h
/usr/include/libqalculate/QalculateDateTime.h
/usr/include/libqalculate/Unit.h
/usr/include/libqalculate/Variable.h
/usr/include/libqalculate/includes.h
/usr/include/libqalculate/qalculate.h
/usr/include/libqalculate/util.h
/usr/lib64/libqalculate.so
/usr/lib64/pkgconfig/libqalculate.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libqalculate/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqalculate.so.21
/usr/lib64/libqalculate.so.21.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libqalculate/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/qalc.1

%files locales -f libqalculate.lang
%defattr(-,root,root,-)

