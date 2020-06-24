# Prevent failure of rpmbuild when mangling shebangs (not entirely sure why the script fails but I believe it's linked to some packaged files having spaces in their filenames, there's an unfixed filezilla bug on that)
%undefine __brp_mangle_shebangs
# Applied to prevent rpmbuild from stripping parts of the PyLNP executable, causing it to fail
# See https://mattsumme.rs/2015/rpmbuild-and-pyinstaller/
%define __os_install_post %{nil}
%define debug_package %{nil}

Name:           lazy-newb-pack
Version:        0.1
Release:        1%{?dist}
Summary:        Enay's Lazy Newb Pack for Dward Fortress

License:        None
URL:            http://www.bay12forums.com/smf/index.php?topic=163211.0
#Source0:        https://dffd.bay12games.com/file.php?id=13244
Patch0:         PyLNP.patch
BuildArch:      x86_64

#BuildRequires:  
Requires:       SDL, SDL_image, SDL_ttf, gtk2-devel, openal-soft, alsa-lib, alsa-plugins-pulseaudio, mesa-dri-drivers, python, gnome-terminal, mono-devel, gtk-sharp2

%description
A ready-to-go rpm package of Enay's Lazy Newb Pack for Dward Fortress

%install
BUILD_DIR=$(pwd)
mkdir -p %{buildroot}/%{_datadir}/%{name}
cd %{buildroot}/%{_datadir}/%{name}
tar -C . -xzf $BUILD_DIR/SOURCES/LinuxLNP-0.47.03-rc1.tar.gz
mv LinuxLNP-0.47.03-rc1/* .
rmdir LinuxLNP-0.47.03-rc1
# Fix permissions problems such as https://github.com/corollari/lazy-newb-pack-fedora/issues/1
# This could be applied more selectively but, at the moment, it works
chmod -R 777 .
# See https://lists.fedoraproject.org/pipermail/packaging/2012-December/008792.html
find . -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +
patch -p1 PyLNP.user $BUILD_DIR/PyLNP.patch
mkdir -p %{buildroot}/%{_bindir}
ln -rs startlnp %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Sat Jun 20 2020 Albert <github@albert.sh>
- 
