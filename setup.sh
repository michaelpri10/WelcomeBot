#!/bin/bash
#
# WelcomeBot setup
#

rev="`git rev-list HEAD --max-count=1 --abbrev-commit 2>/dev/null`"

if [ "$#" -gt 1 ] || ( [ "$#" -eq 1 ] && [ "$1" == "--help" ] ) ;
then
    echo "Set up WelcomeBot."
    echo
    echo "Usage:"
    echo "  $0 [--help | --no-clone]"
    echo
    echo "Options:"
    echo "  --help      Print this help message and exit"
    echo "  --no-clone  Do NOT clone a WelcomeBot git repo (default behavior when inside a repo)"
    exit 1
fi

hello="Setting up WelcomeBot"
if [ "$rev" == "" ] ;
then
    echo "$hello."
else
    echo "$hello (revision: $rev)."
fi

if [ "$1" == "--no-clone" ] && [ "$rev" == "" ] ;
then
    echo "There's nothing to setup. Please obtain a copy of WelcomeBot source code first."
    exit 1
elif [ "$1" == "--no-clone" ] || [ "$rev" != "" ];
then
    echo "Cloning supressed, assuming `pwd` as a WelcomeBot git repo directory."
else
    echo "Cloning WelcomeBot..."
    git clone https://github.com/michaelpri10/WelcomeBot.git michaelpri10/WelcomeBot
    cd "`pwd`/michaelpri10/WelcomeBot"
fi

git submodule update --init
sudo pip install beautifulsoup4
sudo pip install requests --upgrade
sudo pip install websocket-client --upgrade

echo "Setup completed."
exit 0
