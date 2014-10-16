%define oname	xvba-video

Summary:	VA API driver for proprietary fglrx driver
Name:		vaapi-driver-fglrx
Version:	0.8.0
Release:	2
Group:		Video
License:	GPLv2
URL:		http://www.splitted-desktop.com/~gbeauchesne/xvba-video
Source0:	http://www.splitted-desktop.com/~gbeauchesne/xvba-video/%{oname}-%{version}.tar.gz
# for convenience:
Provides:	%{oname} = %{version}-%{release}
BuildRequires:	amd-xvba-devel
BuildRequires:	libva-devel => 1.0.15

%description
XvBA driver backend for VA API, a video acceleration API.

This is a proprietary backend for use with the proprietary fglrx
display driver for ATI cards.


%prep
%setup -q -n %oname-%version

%ifarch x86_64  
sed -i 's|-lXvBAW|-L /usr/lib64/fglrx -lXvBAW|g' configure.ac  
%else  
sed -i 's|-lXvBAW|-L /usr/lib/fglrx -lXvBAW|g' configure.ac  
%endif  

%build
autoreconf -v --install
%configure --with-drivers-path=%{_libdir}/va/drivers
%make


%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/dri/*.la

%files
%doc AUTHORS NEWS
%{_libdir}/dri/*_drv_video.so
