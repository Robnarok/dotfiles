#!/bin/bash

mkdir -p $HOME/.config/i3
ln -f ./i3-config $HOME/.config/i3/config

mkdir -p $HOME/.config/nvim
ln -f ./vim-config.vim $HOME/.config/nvim/init.vim

ln -f ./zsh-config $HOME/.zshrc
