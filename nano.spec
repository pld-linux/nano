Summary:	nano (Nano's ANOther editor)
Summary(pl):	nano - jeszcze jeden edytor
Name:		nano
Version:	1.1.1
Release:	1
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	http://www.nano-editor.org/dist/v1.1/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.nano-editor.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nano (Nano's ANOther editor) is the editor formerly known as TIP (TIP
Isn't Pico). It aims to emulate Pico as closely as possible while also
offering a few enhancements.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog AUTHORS NEWS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/nano
%{_mandir}/man1/*
