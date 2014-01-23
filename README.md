RPM Spec files
==============

RPM Spec files for building correct Oracle JVM RPM packages based on [jpackage](http://www.jpackage.org/develdocs.php#rebuilding) spec 
files.

Preparations for rpmbuild:
--------------------------
    
    sudo yum -y install rpmdevtools && rpmdev-setuptree



Rebuilding from Source:
-----------------------

For building no-src rpm use NoSource option in spec file.

1. Download JDK (.tar.gz, not the rpm package) from [oracle web site](http://www.oracle.com/technetwork/java/) into SOURCES directory
2. Download the time-zone update file (`tzupdater-1_3_62-2013i.zip`) from [Oracle/Downloads](http://www.oracle.com/technetwork/java/javase/downloads/index.html) website into SOURCES dir.
3. Download desired spec file 
4. Download *xsl from SOURCES and place them into local SOURCES directory
5. Rebuild with
```rpmbuild -bb SPECS/java-1.6.0-sun-RELEASE.spec```
