# `$ poeditor2hugo`

[![GitHub version](https://img.shields.io/github/release/Lednerb/poeditor2hugo/all.svg?style=flat-square)](https://github.com/Lednerb/poeditor2hugo/releases)
[![License](https://img.shields.io/github/license/Lednerb/poeditor2hugo.svg?style=flat-square)](https://github.com/Lednerb/poeditor2hugo/blob/master/LICENSE.md)
[![Docker Pulls](https://img.shields.io/docker/pulls/lednerb/poeditor2hugo.svg?style=flat-square)](https://hub.docker.com/r/lednerb/poeditor2hugo/)
[![GitHub stars](https://img.shields.io/github/stars/Lednerb/poeditor2hugo.svg?style=social&label=Stars)](https://github.com/Lednerb/poeditor2hugo)

This tool is for all creators of multilingual Hugo themes.

With `poeditor2hugo` you can easily export your [POEditor](https://poeditor.com) translations to your [Hugo](https://gohugo.io) theme.


## Quickstart with docker

If you have Docker installed, you can simply `cd` into your theme's directory and run:
```
docker run --rm -it -v $PWD:/export lednerb/poeditor2hugo
```

If your current user is not in the `docker` group, you maybe have to run this command with `sudo`.


__Fixing permissions:__

If you are on a Linux system, you might want to change the permissions for the language files.
Within your theme directory run the following command to change the permissions:

```
sudo chown -r $USER:$USER i18n/
```

Alternatively, do it in one step or create a bash alias:

`~/.bashrc`
```
alias poeditor2hugo='sudo docker run --rm -it -v $PWD:/export lednerb/poeditor2hugo && sudo chown -R $USER:$USER i18n'
```

You can then run:
```
cd ~/your/hugo/theme
poeditor2hugo
```

### DEMO
[![DEMO](./demo.gif)](https://github.com/Lednerb/poeditor2hugo/)
