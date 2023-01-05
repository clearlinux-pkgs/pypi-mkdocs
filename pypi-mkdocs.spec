#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-mkdocs
Version  : 1.3.1
Release  : 15
URL      : https://files.pythonhosted.org/packages/52/16/2c2de8fac0437fb81d8f31558111fddcedf56eb56d90dea6ec922fcd588a/mkdocs-1.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/16/2c2de8fac0437fb81d8f31558111fddcedf56eb56d90dea6ec922fcd588a/mkdocs-1.3.1.tar.gz
Summary  : Project documentation with Markdown.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-mkdocs-bin = %{version}-%{release}
Requires: pypi-mkdocs-license = %{version}-%{release}
Requires: pypi-mkdocs-python = %{version}-%{release}
Requires: pypi-mkdocs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(ghp_import)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(markdown)
BuildRequires : pypi(mergedeep)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(pyyaml_env_tag)
BuildRequires : pypi(watchdog)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# MkDocs
> *Project documentation with Markdown*
[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Build Status][GHAction-image]][GHAction-link]
[![Coverage Status][codecov-image]][codecov-link]

%package bin
Summary: bin components for the pypi-mkdocs package.
Group: Binaries
Requires: pypi-mkdocs-license = %{version}-%{release}

%description bin
bin components for the pypi-mkdocs package.


%package license
Summary: license components for the pypi-mkdocs package.
Group: Default

%description license
license components for the pypi-mkdocs package.


%package python
Summary: python components for the pypi-mkdocs package.
Group: Default
Requires: pypi-mkdocs-python3 = %{version}-%{release}

%description python
python components for the pypi-mkdocs package.


%package python3
Summary: python3 components for the pypi-mkdocs package.
Group: Default
Requires: python3-core
Provides: pypi(mkdocs)
Requires: pypi(click)
Requires: pypi(ghp_import)
Requires: pypi(importlib_metadata)
Requires: pypi(jinja2)
Requires: pypi(markdown)
Requires: pypi(mergedeep)
Requires: pypi(packaging)
Requires: pypi(pyyaml)
Requires: pypi(pyyaml_env_tag)
Requires: pypi(watchdog)

%description python3
python3 components for the pypi-mkdocs package.


%prep
%setup -q -n mkdocs-1.3.1
cd %{_builddir}/mkdocs-1.3.1
pushd ..
cp -a mkdocs-1.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672289954
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mkdocs
cp %{_builddir}/mkdocs-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mkdocs/dd3c063a6e112f29876344a5bcd28dc3ee2a73bf || :
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

%files bin
%defattr(-,root,root,-)
/usr/bin/mkdocs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mkdocs/dd3c063a6e112f29876344a5bcd28dc3ee2a73bf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
