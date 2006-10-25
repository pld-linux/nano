%define _pre	pre3
Summary:	nano - Nano's ANOther editor, an enhanced free Pico clone
Summary(pl):	nano - jeszcze jeden edytor, darmowy, rozbudowany klon Pico
Name:		nano
Version:	1.9.99
Release:	0.%{_pre}.1
License:	GPL v2
Group:		Applications/Editors
Source0:	http://www.nano-editor.org/dist/v1.3/%{name}-%{version}%{_pre}.tar.gz
# Source0-md5:	66029c65d23f7e8f721412b1dd28744c
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
nano (Nano's ANOther editor) is a small, free and friendly editor
which aims to replace Pico, the default editor included in the
non-free Pine package. Rather than just copying Pico's look and feel,
nano also implements some missing (or disabled by default) features in
Pico, such as "search and replace" and "go to line number".

%description -l pl
nano to ma³y, otwarty i przyjazny edytor, którego celem jest zast±pienie
Pico, standardowego edytora zawartego w niewolnym pakiecie Pine.
Oprócz wygl±du oraz interfejsu, nano posiada kilka brakuj±cych (lub
wy³±czonych standardowo) w Pico funkcji, takich jak: "znajd¼ i zast±p"
lub "id¼ do linii numer".

%prep
%setup -q -n %{name}-%{version}%{_pre}
%patch0 -p1
%patch1 -p2

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-all
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
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO UPGRADE doc/nanorc.sample doc/faq.html
%attr(755,root,root) %{_bindir}/nano
%{_desktopdir}/nano.desktop
%{_mandir}/man[15]/*
%lang(fr) %{_mandir}/fr/man[15]/*
%{_infodir}/*info*
%{_pixmapsdir}/*
%{_datadir}/nano
