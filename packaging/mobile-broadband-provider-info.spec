Name:           mobile-broadband-provider-info
Version:        20120614
Release:        1
License:        Creative Commons Public Domain
Summary:        Moblie Broadband Dataprovider Database
Url:            http://www.gnome.org
Group:          Applications/Internet
Source0:        %{name}-%{version}.tar.xz
Source101:      mobile-broadband-provider-info-rpmlintrc

%description
This package contains mobile broadband settings for different service providers
in different countries. The Package contains only informational files so it's
safe for distributions to grab updates even during feature freeze and
maintenance stages.

When you want to configure a mobile broadband connections there usually is some
service provider specific information you have to know before the connection
can be established. Problem with this information is that it's highly technical
for an ordinary consumer and it's available only from service providers web
page or from Microsoft Windows installation media that becomes with tie-in
subscription devices.

The interesting side of this information is that it's the same for every user
of a given service provider. This means that service provider specific
information can be stored in a database. When this database is available the
information can be fetched there and the ordinary user does not need to bother
about it.

Service provider specific information is stored in a XML file. XML is not the
most optimized format for a database, but it's easy to read, understand and
edit.

The database is released under Creative Commons Public Domain (CC-PD).

%prep
%setup -q


%build

%configure --disable-static
make %{?_smp_mflags}

%install
%make_install







%files
%license COPYING
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/mobile-broadband-provider-info.pc
%{_datadir}/mobile-broadband-provider-info/*


