#!/bin/bash

# I3
ln -s $PWD/i3 $HOME/.config/.

# Nvim
ln -s $PWD/nvim $HOME/.config/.
touch $HOME/.config/nvim/extra.vim

# zshrc
ln -s $PWD/zsh-config $HOME/.zshrc

#tmux
ln -s $PWD/tmux.conf $HOME/.tmux.conf

#qtile
ln -s $PWD/qtile $HOME/.config/.

#rofi
ln -s $PWD/rofi $HOME/.config/.

#alacritty
ln -s $PWD/alacritty $HOME/.config/.

#xmonad
ln -s $PWD/xmonad $HOME/.config/.

#xmobar
ln -s $PWD/xmobar $HOME/.config/.

#dunst
ln -s $PWD/dunst $HOME/.config/.
