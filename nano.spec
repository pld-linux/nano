Summary:	nano (Nano's ANOther editor)
Summary(pl):	nano - jeszcze jeden edytor
Name:		nano
Version:	1.2.4
Release:	2
License:	GPL
Group:		Applications/Editors
Source0:	http://www.nano-editor.org/dist/v1.2/%{name}-%{version}.tar.gz
# Source0-md5:	2c513310ec5e8b63abaecaf48670ac7a
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-ncurses-ncurses.h.patch
URL:		http://www.nano-editor.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nano (Nano's ANOther editor) is the editor formerly known as TIP (TIP
Isn't Pico). It aims to emulate Pico as closely as possible while also
offering a few enhancements.

%description -l pl
nano to edytor wcze¶niej znany jako TIP (Tip to nIe Pico). Jego celem
jest emulowanie Pico tak dobrze jak to mo¿liwe, jednocze¶nie oferuj±c
kilka rozszerzeñ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing m4/*.m4
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/nano
%{_desktopdir}/nano.desktop
%{_mandir}/man[15]/*
%{_infodir}/*info*
%{_pixmapsdir}/*
