Summary: Basic Archiver
Name: K7Z
Version: 0.6
Release: 1
License: GPL
Packager: Chris Giles
Group: Applications/Archiving
Provides: K7Z
Requires: python >= 2.4, qt4 >= 4.2.2, PyQt4 >= 4.1, p7zip >= 4.30, make >= 3.80, tar >= 1.15
BuildRequires: python >= 2.4, qt4 >= 4.2.2, PyQt4 >= 4.1, p7zip >= 4.30, make >= 3.80, tar >= 1.15
URL: http://k7z.sourceforge.net/
%description
Use K7Z if you want to:
* Backup a folder to a storage location
* Create or extract a password-protected archive
* Update an existing archive quickly

Ark (2.6.3) is very handy but it doesn't seem to:
* Create archives with passwords
* Extract (some) archives with passwords
* Update existing archives by default

K7Z is a simple application that attempts to fill these voids.  It probably won't become a total archiving solution.
%files
%dir "//usr/"
%dir "//usr/bin/"
%dir "//usr/bin/K7Z.pyw"
%dir "//usr/share/"
%dir "//usr/share/icons/"
%dir "//usr/share/icons/hicolor/"
%dir "//usr/share/icons/hicolor/32x32/"
%dir "//usr/share/icons/hicolor/32x32/actions/"
%dir "//usr/share/icons/hicolor/32x32/actions/ark_addfile.png"
%dir "//usr/share/icons/hicolor/32x32/actions/ark_extract.ico"
%dir "//usr/share/icons/hicolor/32x32/actions/ark_extract.png"
%dir "//usr/share/icons/hicolor/32x32/actions/ark_addfile.ico"
%dir "//usr/share/icons/hicolor/32x32/apps/"
%dir "//usr/share/icons/hicolor/32x32/apps/K7Z.ico"
%dir "//usr/share/icons/hicolor/32x32/apps/K7Z.png"
%dir "//usr/share/apps/"
%dir "//usr/share/apps/konqueror/"
%dir "//usr/share/apps/konqueror/servicemenus/"
"//usr/share/apps/konqueror/servicemenus/K7Zc.desktop"
"//usr/share/apps/konqueror/servicemenus/K7Ze.desktop"
%dir "//usr/share/apps/K7Z/"
%dir "//usr/share/apps/K7Z/Desktop/"
%dir "//usr/share/apps/K7Z/Desktop/Context/"
%dir "//usr/share/apps/K7Z/Desktop/Context/Backup/"
"//usr/share/apps/K7Z/Desktop/Context/Backup/K7Ze.desktop.act"
"//usr/share/apps/K7Z/Desktop/Context/Backup/K7Ze.desktop.top"
"//usr/share/apps/K7Z/Desktop/Context/Backup/K7Zc.desktop.act"
"//usr/share/apps/K7Z/Desktop/Context/Backup/K7Z.marker"
"//usr/share/apps/K7Z/Desktop/Context/Backup/K7Zc.desktop.top"
%dir "//usr/share/apps/K7Z/Desktop/Context/Live/"
"//usr/share/apps/K7Z/Desktop/Context/Live/K7Zc.desktop"
"//usr/share/apps/K7Z/Desktop/Context/Live/K7Ze.desktop"
%dir "//usr/share/apps/K7Z/Desktop/KMenu/"
"//usr/share/apps/K7Z/Desktop/KMenu/K7Z.desktop"
%dir "//usr/share/apps/K7Z/Desktop/Profiles/"
"//usr/share/apps/K7Z/Desktop/Profiles/Default.txt"
"//usr/share/apps/K7Z/Desktop/Profiles/Storage.txt"
"//usr/share/apps/K7Z/Desktop/Profiles/Secure.txt"
%dir "//usr/share/apps/K7Z/Source/"
"//usr/share/apps/K7Z/Source/K7Z.pyw"
"//usr/share/apps/K7Z/Source/Help.py"
"//usr/share/apps/K7Z/Source/Main_rc.py"
"//usr/share/apps/K7Z/Source/Main.py"
"//usr/share/apps/K7Z/Source/Settings.py"
"//usr/share/apps/K7Z/Source/Input.py"
"//usr/share/apps/K7Z/Source/Settings.qrc"
"//usr/share/apps/K7Z/Source/Thread.py"
"//usr/share/apps/K7Z/Source/Main.ui"
"//usr/share/apps/K7Z/Source/Main.qrc"
"//usr/share/apps/K7Z/Source/Main_ui.py"
"//usr/share/apps/K7Z/Source/Profile.py"
"//usr/share/apps/K7Z/Source/Import.py"
"//usr/share/apps/K7Z/Source/Settings.ui"
%dir "//usr/share/apps/K7Z/Source/Images/"
%dir "//usr/share/apps/K7Z/Source/Images/devices/"
"//usr/share/apps/K7Z/Source/Images/devices/dvd_unmount.png"
"//usr/share/apps/K7Z/Source/Images/devices/3floppy_unmount.png"
"//usr/share/apps/K7Z/Source/Images/devices/hdd_unmount.png"
"//usr/share/apps/K7Z/Source/Images/devices/cdrom_unmount.png"
%dir "//usr/share/apps/K7Z/Source/Images/actions/"
"//usr/share/apps/K7Z/Source/Images/actions/1downarrow.png"
"//usr/share/apps/K7Z/Source/Images/actions/fileclose.png"
"//usr/share/apps/K7Z/Source/Images/actions/K7Z-ledgreen.png"
"//usr/share/apps/K7Z/Source/Images/actions/endturn.png"
"//usr/share/apps/K7Z/Source/Images/actions/exit.png"
"//usr/share/apps/K7Z/Source/Images/actions/ark_addfile.png"
"//usr/share/apps/K7Z/Source/Images/actions/revert.png"
"//usr/share/apps/K7Z/Source/Images/actions/button_ok.png"
"//usr/share/apps/K7Z/Source/Images/actions/filesaveas.png"
"//usr/share/apps/K7Z/Source/Images/actions/1uparrow.png"
"//usr/share/apps/K7Z/Source/Images/actions/2downarrow.png"
"//usr/share/apps/K7Z/Source/Images/actions/K7Z-ledred.png"
"//usr/share/apps/K7Z/Source/Images/actions/ark_extract.ico"
"//usr/share/apps/K7Z/Source/Images/actions/edit_remove.png"
"//usr/share/apps/K7Z/Source/Images/actions/ark_extract.png"
"//usr/share/apps/K7Z/Source/Images/actions/reload.png"
"//usr/share/apps/K7Z/Source/Images/actions/2uparrow.png"
"//usr/share/apps/K7Z/Source/Images/actions/edit_add.png"
"//usr/share/apps/K7Z/Source/Images/actions/button_cancel.png"
"//usr/share/apps/K7Z/Source/Images/actions/ark_addfile.ico"
"//usr/share/apps/K7Z/Source/Images/actions/endturn.ico"
"//usr/share/apps/K7Z/Source/Images/actions/filesave.png"
"//usr/share/apps/K7Z/Source/Images/actions/stop.png"
"//usr/share/apps/K7Z/Source/Images/actions/1leftarrow.png"
"//usr/share/apps/K7Z/Source/Images/actions/fileopen.png"
%dir "//usr/share/apps/K7Z/Source/Images/filesystems/"
"//usr/share/apps/K7Z/Source/Images/filesystems/folder.png"
"//usr/share/apps/K7Z/Source/Images/filesystems/folder_tar.png"
%dir "//usr/share/apps/K7Z/Source/Images/mimetypes/"
"//usr/share/apps/K7Z/Source/Images/mimetypes/Zip.png"
"//usr/share/apps/K7Z/Source/Images/mimetypes/Tar.png"
"//usr/share/apps/K7Z/Source/Images/mimetypes/7-Zip.png"
"//usr/share/apps/K7Z/Source/Images/mimetypes/GZip.png"
"//usr/share/apps/K7Z/Source/Images/mimetypes/txt.png"
"//usr/share/apps/K7Z/Source/Images/mimetypes/BZip2.png"
%dir "//usr/share/apps/K7Z/Source/Images/apps/"
"//usr/share/apps/K7Z/Source/Images/apps/ckhome2.png"
"//usr/share/apps/K7Z/Source/Images/apps/gnu-head-sm.jpg"
"//usr/share/apps/K7Z/Source/Images/apps/fmtools-ico32.png"
"//usr/share/apps/K7Z/Source/Images/apps/qt4-logo.png"
"//usr/share/apps/K7Z/Source/Images/apps/python-logo.png"
"//usr/share/apps/K7Z/Source/Images/apps/package_settings.png"
"//usr/share/apps/K7Z/Source/Images/apps/K7Z.ico"
"//usr/share/apps/K7Z/Source/Images/apps/pyqt-logo.png"
"//usr/share/apps/K7Z/Source/Images/apps/K7Z.png"
"//usr/share/apps/K7Z/Source/Settings_rc.py"
"//usr/share/apps/K7Z/Source/Settings_ui.py"
%dir "//usr/share/apps/K7Z/Doc/"
"//usr/share/apps/K7Z/Doc/ChangeLog.txt"
%dir "//usr/share/apps/K7Z/Doc/COPYING.txt"
"//usr/share/apps/K7Z/Doc/ISSUES.txt"
"//usr/share/apps/K7Z/Doc/Testing.txt"
"//usr/share/apps/K7Z/Doc/LICENCE.txt"
"//usr/share/apps/K7Z/Doc/NEWS.txt"
"//usr/share/apps/K7Z/Doc/TODO.txt"
"//usr/share/apps/K7Z/Doc/AUTHORS.txt"
"//usr/share/apps/K7Z/Doc/INSTALL.txt"
"//usr/share/apps/K7Z/Doc/README.txt"
%dir "//usr/share/applnk/"
%dir "//usr/share/applnk/Utilities/"
%dir "//usr/share/applnk/Utilities/File/"
"//usr/share/applnk/Utilities/File/K7Z.desktop"
