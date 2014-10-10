# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kwallet

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 solution for password management
Version:    5.3.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kwallet.yaml
Source101:  kwallet-rpmlintrc
Requires:   kf5-filesystem
Requires:   kwallet-libs%{?_isa} = %{version}-%{release}
Requires:   kwallet-runtime%{?_isa} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libgpg-error)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kconfig-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  knotifications-devel
BuildRequires:  kservice-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel

%description
KDE Frameworks 5 Tier 3 solution for password management


%package libs
Summary:    KWallet framework libraries
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kf5-filesystem
Provides:   kwallet-api = %{version}-%{release}
Provides:   kwallet-api%{?_isa} = %{version}-%{release}

%description libs
Provides API to access KWallet data from applications.


%package runtime
Summary:    KWallet runtime deamon
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description runtime
Provides a runtime deamon that stores passwords.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kwallet-libs%{?_isa} = %{version}-%{release}
Requires:   kconfig-devel
Requires:   kwindowsystem-devel
Requires:   kcoreaddons-devel
Requires:   kdbusaddons-devel
Requires:   ki18n-devel
Requires:   kiconthemes-devel
Requires:   knotifications-devel
Requires:   kservice-devel
Requires:   kwidgetsaddons-devel
Requires:   kwindowsystem-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%find_lang kwallet5_qt --with-qt --all-name || :

%files -f kwallet5_qt.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
# >> files
# << files

%files libs
%defattr(-,root,root,-)
%{_kf5_libdir}/libKF5Wallet.so.*
%{_kf5_libdir}/libkwalletbackend5.so.*
# >> files libs
# << files libs

%files runtime
%defattr(-,root,root,-)
%{_kf5_sharedir}/dbus-1/services/*
%{_kf5_bindir}/kwalletd5
%{_kf5_servicesdir}/kwalletd5.desktop
%{_kf5_sharedir}/knotifications5/kwalletd.notifyrc
# >> files runtime
# << files runtime

%files devel
%defattr(-,root,root,-)
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KWallet.xml
%{_kf5_includedir}/kwallet_version.h
%{_kf5_includedir}/KWallet
%{_kf5_cmakedir}/KF5Wallet
%{_kf5_libdir}/libKF5Wallet.so
%{_kf5_libdir}/libkwalletbackend5.so
%{_kf5_mkspecsdir}/qt_KWallet.pri
# >> files devel
# << files devel
