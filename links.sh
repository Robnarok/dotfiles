#!/bin/bash

# I3
mkdir -p $HOME/.config/i3
ln -s $PWD/i3-config $HOME/.config/i3/config

# Nvim
mkdir -p $HOME/.config/nvim
ln -s $PWD/vim-config.vim $HOME/.config/nvim/init.vim
touch $HOME/.config/nvim/extra.vim

# zshrc
ln -s $PWD/zsh-config $HOME/.zshrc

#tmux
ln -s $PWD/tmux.conf $HOME/.tmux.conf
