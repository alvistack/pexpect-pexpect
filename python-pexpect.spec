# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pexpect
Epoch: 100
Version: 4.8.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Unicode-aware Pure Python Expect-like module
License: BSD-3-Clause
URL: https://github.com/pexpect/pexpect/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Pexpect is a pure Python module for spawning child applications;
controlling them; and responding to expected patterns in their output.
Pexpect works like Don Libes' Expect. Pexpect allows your script to
spawn a child application and control it as if a human were typing
commands.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pexpect
Summary: Unicode-aware Pure Python Expect-like module
Requires: python3
Requires: python3-ptyprocess >= 0.5
Provides: python3-pexpect = %{epoch}:%{version}-%{release}
Provides: python3dist(pexpect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pexpect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pexpect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pexpect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pexpect) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pexpect
Pexpect is a pure Python module for spawning child applications;
controlling them; and responding to expected patterns in their output.
Pexpect works like Don Libes' Expect. Pexpect allows your script to
spawn a child application and control it as if a human were typing
commands.

%files -n python%{python3_version_nodots}-pexpect
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pexpect
Summary: Unicode-aware Pure Python Expect-like module
Requires: python3
Requires: python3-ptyprocess >= 0.5
Provides: python3-pexpect = %{epoch}:%{version}-%{release}
Provides: python3dist(pexpect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pexpect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pexpect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pexpect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pexpect) = %{epoch}:%{version}-%{release}

%description -n python3-pexpect
Pexpect is a pure Python module for spawning child applications;
controlling them; and responding to expected patterns in their output.
Pexpect works like Don Libes' Expect. Pexpect allows your script to
spawn a child application and control it as if a human were typing
commands.

%files -n python3-pexpect
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
