#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-minikanren
Version  : 1.0.3
Release  : 9
URL      : https://files.pythonhosted.org/packages/c8/21/1be8af0ecaf5a61abebabc8dabf63a08d72334ced5bb9f9d027fd7abbf42/miniKanren-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/c8/21/1be8af0ecaf5a61abebabc8dabf63a08d72334ced5bb9f9d027fd7abbf42/miniKanren-1.0.3.tar.gz
Summary  : Relational programming in Python
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-minikanren-license = %{version}-%{release}
Requires: pypi-minikanren-python = %{version}-%{release}
Requires: pypi-minikanren-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cons)
BuildRequires : pypi(etuples)
BuildRequires : pypi(logical_unification)
BuildRequires : pypi(multipledispatch)
BuildRequires : pypi(toolz)

%description
# `kanren`
[![Build Status](https://travis-ci.org/pythological/kanren.svg?branch=master)](https://travis-ci.org/pythological/kanren) [![Coverage Status](https://coveralls.io/repos/github/pythological/kanren/badge.svg?branch=master)](https://coveralls.io/github/pythological/kanren?branch=master) [![PyPI](https://img.shields.io/pypi/v/miniKanren)](https://pypi.org/project/miniKanren/)

%package license
Summary: license components for the pypi-minikanren package.
Group: Default

%description license
license components for the pypi-minikanren package.


%package python
Summary: python components for the pypi-minikanren package.
Group: Default
Requires: pypi-minikanren-python3 = %{version}-%{release}

%description python
python components for the pypi-minikanren package.


%package python3
Summary: python3 components for the pypi-minikanren package.
Group: Default
Requires: python3-core
Provides: pypi(minikanren)
Requires: pypi(cons)
Requires: pypi(etuples)
Requires: pypi(logical_unification)
Requires: pypi(multipledispatch)
Requires: pypi(toolz)

%description python3
python3 components for the pypi-minikanren package.


%prep
%setup -q -n miniKanren-1.0.3
cd %{_builddir}/miniKanren-1.0.3
pushd ..
cp -a miniKanren-1.0.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394110
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-minikanren
cp %{_builddir}/miniKanren-1.0.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-minikanren/e116414ac1a00c287445bcd5ff397fc71c5aec57
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-minikanren/e116414ac1a00c287445bcd5ff397fc71c5aec57

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
