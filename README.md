RPM Spec files
==============

Collection of RPM `.spec` files for a number of popular and/or abandoned rpmbuild
projects

This project aims to facilitate the continuation of abandoned projects with
respect to the creation and/or compilation of rpm-packages of popular programs
and applications; one such program is Mozilla's 
[Firefox-Aurora](http://www.mozilla.org/en-US/firefox/aurora/),
or the nightly build of Firefox, which is not hosted in most distributions' 
repositories.


RPM Spec files for building correct Oracle JVM RPM packages based on
[jpackage](http://www.jpackage.org/develdocs.php#rebuilding) spec 
files.

Preparations for rpmbuild:
--------------------------
    
    sudo yum -y install rpmdevtools && rpmdev-setuptree



Rebuilding oracle jdk from Source:
-----------------------

For building no-src rpm use NoSource option in spec file.

1. Download JDK (.tar.gz, not the rpm package) from [oracle web site](http://www.oracle.com/technetwork/java/) into SOURCES directory
2. Download the time-zone update file (`tzupdater-1_3_62-2013i.zip`) from [Oracle/Downloads](http://www.oracle.com/technetwork/java/javase/downloads/index.html) website into SOURCES dir.
3. Download desired spec file 
4. Download *xsl from SOURCES and place them into local SOURCES directory
5. Rebuild with
```rpmbuild -bb SPECS/java-1.6.0-sun-RELEASE.spec```
