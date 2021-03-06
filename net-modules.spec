# This file is © 2015 Mesosphere, Inc. ("Mesosphere"). Mesosphere
# licenses this file to you solely pursuant to the agreement between
# Mesosphere and you (if any).  If there is no such agreement between
# Mesosphere, the following terms apply (and you may not use this
# file except in compliance with such terms):
#
# 1) Subject to your compliance with the following terms, Mesosphere
# hereby grants you a nonexclusive, limited, personal,
# non-sublicensable, non-transferable, royalty-free license to use
# this file solely for your internal business purposes.
#
# 2) You may not (and agree not to, and not to authorize or enable
# others to), directly or indirectly:
#   (a) copy, distribute, rent, lease, timeshare, operate a service
#   bureau, or otherwise use for the benefit of a third party, this
#   file; or
#
#   (b) remove any proprietary notices from this file.  Except as
#   expressly set forth herein, as between you and Mesosphere,
#   Mesosphere retains all right, title and interest in and to this
#   file.
#
# 3) Unless required by applicable law or otherwise agreed to in
# writing, Mesosphere provides this file on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
# including, without limitation, any warranties or conditions of
# TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
# PARTICULAR PURPOSE.
#
# 4) In no event and under no legal theory, whether in tort
# (including negligence), contract, or otherwise, unless required by
# applicable law (such as deliberate and grossly negligent acts) or
# agreed to in writing, shall Mesosphere be liable to you for
# damages, including any direct, indirect, special, incidental, or
# consequential damages of any character arising as a result of these
# terms or out of the use or inability to use this file (including
# but not limited to damages for loss of goodwill, work stoppage,
# computer failure or malfunction, or any and all other commercial
# damages or losses), even if Mesosphere has been advised of the
# possibility of such damages.

Name:           net-modules
Version:        0.1
Release:        0%{?dist}
License:        Mesosphere
Summary:        Network isolator module
Url:            https://github.com/mesosphere/net-modules
Source0:        net-modules-0.1.tar.gz

# This package is functional only on i386 and x86_64 architectures.
ExclusiveArch:	%ix86 x86_64

%description
Network isolator module.

%prep
%setup -q

%build
# Replace $HOME/usr with your Mesos install location (/usr/local).
%configure --with-mesos=$HOME/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%{_libdir}/mesos

%changelog
* Wed May 6 2015 Kapil Arya <kapil@mesosphere.io> - 0.1
- Preparing for initial packaging.

