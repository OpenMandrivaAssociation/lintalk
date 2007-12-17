%define name	lintalk
%define version	0.4
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	Serverless instant messaging for a LAN
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}-1.tar.bz2
URL:		http://software.manicsadness.com
License:	GPLv2+
Group:		Networking/Chat
BuildRequires:	gtk2-devel pkgconfig

%description
LinTalk is a simple serverless instant messaging tool which is primarily meant
for Local Area Networks. The contactlists synchronize automatically between
all known hosts.

%prep
%setup -q

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/usr/doc

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=networking_section
Terminal=false
Type=Application
Categories=GTK;Network;InstantMessaging;
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ABOUT-NLS AUTHORS ChangeLog NEWS TODO
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
