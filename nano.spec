Summary:	nano (Nano's ANOther editor)
Summary(pl):	nano - jeszcze jeden edytor
Name:		nano
Version:	1.1.10
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://www.nano-editor.org/dist/v1.1/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-info.patch
URL:		http://www.nano-editor.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nano (Nano's ANOther editor) is the editor formerly known as TIP (TIP
Isn't Pico). It aims to emulate Pico as closely as possible while also
offering a few enhancements.

%description -l pl
nano to edytor wcześniej znany jako TIP (Tip to nIe Pico). Jego celem
jest emulowanie Pico tak dobrze jk to możliwe, jednocześnie oferując
kilka rozszerzeń.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing m4/*.m4
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%{_mandir}/man1/*
%{_infodir}/*info*
