Summary:	GNU nano - Nano's ANOther editor, an enhanced free Pico clone
Summary(pl.UTF-8):	GNU nano - jeszcze jeden edytor: darmowy, rozbudowany klon Pico
Name:		nano
Version:	4.5
Release:	1
License:	GPL v3+
Group:		Applications/Editors
Source0:	https://www.nano-editor.org/dist/latest/%{name}-%{version}.tar.xz
# Source0-md5:	686a169b6e5e1f76fe79570f07934001
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-ncurses-ncurses.h.patch
URL:		http://www.nano-editor.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
BuildRequires:	gettext-tools >= 0.18.3
BuildRequires:	groff
BuildRequires:	libmagic-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU nano (Nano's ANOther editor) is a small, free and friendly editor
which aims to replace Pico, the default editor included in the
non-free Pine package. Rather than just copying Pico's look and feel,
nano also implements some missing (or disabled by default) features in
Pico, such as "search and replace" and "go to line number".

%description -l pl.UTF-8
GNU nano (Nano's ANOther editor - Nano to kolejny edytor) to mały,
otwarty i przyjazny edytor, którego celem jest zastąpienie Pico,
standardowego edytora zawartego w niewolnym pakiecie Pine. Oprócz
wyglądu oraz interfejsu, nano posiada kilka brakujących (lub
wyłączonych standardowo) w Pico funkcji, takich jak: "znajdź i zastąp"
lub "idź do wiersza numer".

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
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

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog IMPROVEMENTS NEWS README THANKS TODO doc/{faq.html,sample.nanorc}
%attr(755,root,root) %{_bindir}/nano
%attr(755,root,root) %{_bindir}/rnano
%{_datadir}/nano
%{_desktopdir}/nano.desktop
%{_pixmapsdir}/nano.png
%{_mandir}/man1/nano.1*
%{_mandir}/man1/rnano.1*
%{_mandir}/man5/nanorc.5*
%{_infodir}/nano.info*
