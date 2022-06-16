#!/bin/bash

# I3
mkdir -p $HOME/.config/i3
ln -f ./i3-config $HOME/.config/i3/config

# Nvim
mkdir -p $HOME/.config/nvim
ln -f ./vim-config.vim $HOME/.config/nvim/init.vim
touch $HOME/.config/nvim/extra.vim

# zshrc
ln -f ./zsh-config $HOME/.zshrc
