# Lazy Newb Pack's rpm package
> A ready-to-go rpm package of Enay's Lazy Newb Pack for Dward Fortress

## Install
Download the latest rpm package from [the releases page](https://github.com/corollari/lazy-newb-pack-fedora/releases) and install it with:
```
sudo dnf install ./lazy-newb-pack-0.1-1.fc32.x86_64.rpm
```

Afterwards, the following command can be used to run it:
```
lazy-newb-pack
```

## Package
If you'd like to build the package yourself (not required if you just want to install it), you can do so by downloading the latest version of the pack from [its source](https://dffd.bay12games.com/file.php?id=13244), putting the downloaded file inside the `SOURCES` folder and running the following command:
```
fedpkg --release f32 local
```
