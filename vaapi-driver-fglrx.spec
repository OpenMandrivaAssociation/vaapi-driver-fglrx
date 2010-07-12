
%define name	vaapi-driver-fglrx
%define oname	xvba-video
%define version	0.7.1
%define rel	1

Summary:	VA API driver for proprietary fglrx driver
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Group:		Video
License:	Freeware
URL:		http://www.splitted-desktop.com/~gbeauchesne/xvba-video/
Source0:	http://www.splitted-desktop.com/~gbeauchesne/xvba-video/%{oname}-%{version}.i686.tar.gz
Source1:	http://www.splitted-desktop.com/~gbeauchesne/xvba-video/%{oname}-%{version}.x86_64.tar.gz
# for convenience:
Provides:	%{oname}
ExclusiveArch:	%ix86 x86_64

%description
XvBA driver backend for VA API, a video acceleration API.

This is a proprietary backend for use with the proprietary fglrx
display driver for ATI cards.

%prep
%ifarch %ix86
%setup -q -n %oname-%version.i686 -T -b 0
%else
%setup -q -n %oname-%version.x86_64 -T -b 1
%endif

%install
rm -rf %{buildroot}

install -d -m755 %{buildroot}%{_libdir}/va/drivers
cp -a usr/lib/va/drivers/* %{buildroot}%{_libdir}/va/drivers

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_libdir}/va/drivers/*_drv_video.so
