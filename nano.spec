Summary:	nano (Nano's ANOther editor)
Name:		nano
Version:	0.9.6
Release:	1
License:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source0:	http://www.asty.org/nano/dist/%{name}-%{version}.tar.gz
URL:		http://www.asty.org/nano/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nano (Nano's ANOther editor) is the editor formerly known as TIP (TIP Isn't
Pico). It aims to emulate Pico as closely as possible while also offering a
few enhancements.  %Prep

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
export LDFLAGS CFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README ChangeLog AUTHORS NEWS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/nano
%{_mandir}/man1/*
