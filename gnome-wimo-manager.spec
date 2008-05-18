Summary:	GNOME-WiMo-Manager
Name:		gnome-wimo-manager
Version:	0.6.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/wimo/%{name}-%{version}.tar.bz2
# Source0-md5:	0f11cce9c24c3c697b1f8c915ce19668
URL:		http://www.wimol.org/
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.7
BuildRequires:	dotnet-gnome-sharp-devel >= 2.7
BuildRequires:	mono-csharp
BuildRequires:	nant
BuildRequires:	pkgconfig
BuildRequires:	wimo-rapi
Requires:	wimo-rapi
Requires:	wimo-dbus
Requires:	wimo-dccm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Windows Mobile devices support for Linux desktop.

GNOME WiMo manager - It's purpose is to notify user about connected
and disconnected PocketPC devices and to ask user for device password.
And is creating and deleting PocketPC connection files.

%prep
%setup -q

%build
nant -D:PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
nant install \
	-D:DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/autostart/%{name}.desktop
%{_pixmapsdir}/gnome-pocketpc.png
%{_libdir}/%{name}
