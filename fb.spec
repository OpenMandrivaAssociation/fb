%define name fb
%define version 1.5
%define release %mkrel 14

Summary: Utility for the viewing, editing, and manipulation of binary files
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Source0: fb_tar.bz2
Source1: http://home.mho.net/jswaby/fb_exmp.html
Group: File tools
URL: http://home.mho.net/jswaby/fb.html 
Buildroot: %{_tmppath}/%{name}-buildroot

%description
fb is a binary file viewer, editor, and manipulator. It can be used as a 
filter, an interactive browser, or to simply dump a file in either binary, 
decimal, hexadecimal, or octal and/or characters. Either overwrite bytes in 
either of the four bases or characters or dump to a file and edit the 
resulting text file with any text editor, then fb can translate from either 
of the four bases back into a binary file. In summary, fb is a versatile 
tool for binary file creation, manipulation, and examination. 
Author: John Howard Swaby <polymath@uwyo.edu> 

%prep 

%setup0 -q -c 
cp $RPM_SOURCE_DIR/fb_exmp.html $RPM_BUILD_DIR/$RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION

%build
cc $RPM_OPT_FLAGS fb.c -o fb

%install
rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 fb $RPM_BUILD_ROOT%{_bindir}/
install -m 644 fb.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files 
%defattr (-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%doc README fb.doc fb_exmp.html

%clean
rm -rf $RPM_BUILD_ROOT

