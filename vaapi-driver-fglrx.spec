
%define name	vaapi-driver-fglrx
%define oname	xvba-video
%define version	0.7.6
%define rel	1

Summary:	VA API driver for proprietary fglrx driver
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
Group:		Video
License:	Freeware
URL:		http://www.splitted-desktop.com/~gbeauchesne/xvba-video/
Source0:	http://www.splitted-desktop.com/~gbeauchesne/xvba-video/%{oname}-%{version}.bin.tar.gz
# for convenience:
Provides:	%{oname}
ExclusiveArch:	%ix86 x86_64

%description
XvBA driver backend for VA API, a video acceleration API.

This is a proprietary backend for use with the proprietary fglrx
display driver for ATI cards.

%prep
%setup -q -n %oname-%version.bin

%install
rm -rf %{buildroot}

install -d -m755 %{buildroot}%{_libdir}/va/drivers
%ifarch %ix86
cp -a x86/* \
%endif
%ifarch x86_64
cp -a x64/* \
%endif
	%{buildroot}%{_libdir}/va/drivers

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_libdir}/va/drivers/*_drv_video.so
