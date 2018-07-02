#!/bin/bash
code --install-extension eamodio.gitlens
code --install-extension ms-python.python
code --install-extension sandy081.todotasks
code --install-extension yzhang.markdown-all-in-one
code --install-extension zhuangtongfa.material-theme

sudo apt install inkscape
sudo apt upgrade -y

https://repo.anaconda.com/archive/Anaconda2-5.2.0-Linux-x86_64.sh
bash Anaconda2-5.2.0-Linux-x86_64.sh

# jupyter notebook --ip=0.0.0.0 --notebook-dir=/media/sf_Users/Documents/git/ --no-browser --port=8889


tar -xzf install-tl-unx.tar.gz 
sudo ./install-tl -gui text
PATH=/usr/local/texlive/2018/bin/i386-linux:$PATH
PATH=/usr/local/texlive/2018/bin/x86_64-linux:$PATH
INFOPATH=/usr/local/texlive/2018/texmf-dist/doc/info:$INFOPATH
MANPATH=/usr/local/texlive/2018/texmf-dist/doc/man:$MANPATH

# This updates VS Code:
sudo apt update && sudo apt upgrade code