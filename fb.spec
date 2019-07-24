%define name fb
%define version 1.5
%define release 15

Summary: Utility for the viewing, editing, and manipulation of binary files
Name: %{name}
Version:	2.0.4
Release:	1
License: GPLv1
Source0: fb_tar.bz2
Source1: fb_exmp.html
Group: File tools
URL: http://home.mho.net/jswaby/fb.html 


%description
fb is a binary file viewer, editor, and manipulator. It can be used as a 
filter, an interactive browser, or to simply dump a file in either binary, 
decimal, hexadecimal, or octal and/or characters. Either overwrite bytes in 
either of the four bases or characters or dump to a file and edit the 
resulting text file with any text editor, then fb can translate from either 
of the four bases back into a binary file. In summary, fb is a versatile 
tool for binary file creation, manipulation, and examination. 
 

%prep 
%setup0 -q -c 
cp %SOURCE1 $RPM_BUILD_DIR/%{name}-%{version}

%build
cc $RPM_OPT_FLAGS fb.c -o fb

%install
install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 fb $RPM_BUILD_ROOT%{_bindir}/
install -m 644 fb.1 $RPM_BUILD_ROOT%{_mandir}/man1/


%files 
%{_bindir}/*
%{_mandir}/man1/*
%doc README fb.doc fb_exmp.html





%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-14mdv2011.0
+ Revision: 618256
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.5-13mdv2010.0
+ Revision: 428707
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5-12mdv2009.0
+ Revision: 245059
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.5-10mdv2008.1
+ Revision: 136408
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import fb


* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 1.5-10mdv2007.0
- rebuild

* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 1.5-9mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.5-8mdk
- rebuild

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5-7mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.5-6mdk
- rebuild

* Fri Jul 06 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5-5mdk
- rebuild

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5-4mdk
- rebuild

* Tue Aug 01 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.5-3mdk
- BM

* Wed Apr 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.5-2mdk
- fix group
- spec helper fixes

* Thu Feb 17 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build

