#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-mkdocs
Version  : 1.5.3
Release  : 25
URL      : https://files.pythonhosted.org/packages/ed/bb/24a22f8154cf79b07b45da070633613837d6e59c7d870076f693b7b1c556/mkdocs-1.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ed/bb/24a22f8154cf79b07b45da070633613837d6e59c7d870076f693b7b1c556/mkdocs-1.5.3.tar.gz
Summary  : Project documentation with Markdown.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-mkdocs-bin = %{version}-%{release}
Requires: pypi-mkdocs-license = %{version}-%{release}
Requires: pypi-mkdocs-python = %{version}-%{release}
Requires: pypi-mkdocs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(babel)
BuildRequires : pypi(hatchling)
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
Requires: pypi(jinja2)
Requires: pypi(markdown)
Requires: pypi(markupsafe)
Requires: pypi(mergedeep)
Requires: pypi(packaging)
Requires: pypi(pathspec)
Requires: pypi(platformdirs)
Requires: pypi(pyyaml)
Requires: pypi(pyyaml_env_tag)
Requires: pypi(watchdog)

%description python3
python3 components for the pypi-mkdocs package.


%prep
%setup -q -n mkdocs-1.5.3
cd %{_builddir}/mkdocs-1.5.3
pushd ..
cp -a mkdocs-1.5.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695141231
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . markdown
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . markdown
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mkdocs
cp %{_builddir}/mkdocs-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mkdocs/dd3c063a6e112f29876344a5bcd28dc3ee2a73bf || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} markdown
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
