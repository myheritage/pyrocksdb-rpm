# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
#%{?scl:%scl_package pyrocksdb}
%define gh_owner elad
%define gh_project pyrocksdb
%define pkg_name %{gh_project}

Name:           python-pyrocksdb
Version:        0.5 
Release:        %{?release}%{!?release:1}%{?dist}
Summary: Python bindings for RocksDB       

License: BSD        
URL: https://github.com/elad/pyrocksdb/ 
Source0: https://github.com/%{gh_owner}/%{gh_project}/archive/v%{version}.tar.gz#/%{gh_project}-%{version}.tar.gz

BuildRequires:  python-devel, python-setuptools, rocksdb-devel, %{?scl_prefix}gcc >= 4.8.2, %{?scl_prefix}binutils, %{?scl_prefix}gcc-c++ >= 4.8.2, Pyrex, Cython >= 0.24.1
Requires:  python, rocksdb

%description


%prep
%setup -n %{pkg_name}-%{version} -q

%build
%{?scl:scl enable %{scl} - << \EOF}
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
%{?scl:EOF}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc
# For arch-specific packages: sitearch
%{python_sitearch}/*


%changelog
* Mon Jul 25 2016 Imri Zvik
- 
