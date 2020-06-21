%undefine __brp_mangle_shebangs

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
Requires:       SDL, SDL_image, SDL_ttf, gtk2-devel, openal-soft, alsa-lib, alsa-plugins-pulseaudio, mesa-dri-drivers, python, gnome-terminal

%description
A ready-to-go rpm package of Enay's Lazy Newb Pack for Dward Fortress

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
pwd
tar -C %{buildroot}/%{_datadir}/%{name} -xzf SOURCES/LinuxLNP-0.47.03-rc1.tar.gz
mv %{buildroot}/%{_datadir}/%{name}/LinuxLNP-0.47.03-rc1/* %{buildroot}/%{_datadir}/%{name}
rmdir %{buildroot}/%{_datadir}/%{name}/LinuxLNP-0.47.03-rc1
# See https://lists.fedoraproject.org/pipermail/packaging/2012-December/008792.html
find %buildroot -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +
# This could be applied more selectively but, at the moment, it works
chmod -R 755 %{buildroot}/%{_datadir}/%{name}
# Make data folder writable
chmod -R 777 %{buildroot}/%{_datadir}/%{name}/df_linux/data
chmod -R 777 %{buildroot}/%{_datadir}/%{name}/PyLNP.user
patch -p1 %{buildroot}/%{_datadir}/%{name}/PyLNP.user PyLNP.patch
mkdir -p %{buildroot}/%{_bindir}
ln -rs %{buildroot}/%{_datadir}/%{name}/startlnp %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
"%{_datadir}/%{name}/"
%{_datadir}/%{name}/df_linux/hack/libprotobuf-lite.so

%changelog
* Sat Jun 20 2020 Albert <github@albert.sh>
- 
