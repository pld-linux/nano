Summary: nano (Nano's ANOther editor) is the editor formerly known as TIP (TIP Isn't Pico). It aims to emulate Pico as closely as possible while also offering a few enhancements.
Name: nano
Version: 0.8.9
Release: 1
Group: Console/Editors
Copyright: GPL
Packager: chrisa@asty.org
URL: http://www.asty.org/nano/
Source0: http://www.asty.org/nano/dist/nano-0.8.9.tar.gz
#Provides: none
Requires: ncurses
#Conflicts: none
BuildRoot: /tmp/nano-0.8.9
%Description
nano (Nano's ANOther editor) is the editor formerly known as TIP (TIP Isn't 
Pico). It aims to emulate Pico as closely as possible while also offering a few enhancements.
%Prep
%setup
%Build
./configure --prefix=/usr
make
%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1/
strip nano
install nano $RPM_BUILD_ROOT/usr/bin
install nano.1 $RPM_BUILD_ROOT/usr/man/man1
%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(-,root,root)
/usr/bin/nano
/usr/man/man1/nano.1
%doc README COPYING ChangeLog AUTHORS BUGS INSTALL NEWS TODO nano.1.html
%doc COPYING
%doc ChangeLog
%doc AUTHORS
%doc BUGS
%doc INSTALL
%doc NEWS
%doc TODO
%doc nano.1.html
