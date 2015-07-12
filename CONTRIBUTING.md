# Contributing guidelines

WelcomeBot welcomes your pull requests!

When creating a pull request, please take the code styling guidelines in account, as specified in this document.

The first, and most important rule is the indentation: you have to use 4 spaces for indentation, no tabs.

Your code has to be conform to the PEP styling guidelines. An easy way to check whether it is, is to install the tool [Flake8](https://pypi.python.org/pypi/flake8) (`pip install flake8`) and to run it in the directory of the bot:

    flake8 ./

When running that command, Flake8 will look at the `tox.ini` file. This file contains rules to exclude the following warnings:

 - E501: Flake8 gives this error when a line is longer than 80 chars. Having a line that's longer than this is not a big problem for WelcomeBot.
 - F403: Flake8 gives this warning when it comes across a star import (`from <module> import *`), because it cannot check whether all imported methods are used.

`tox.ini` also excludes a few directories which shouldn't be checked.

The Contributors of WelcomeBot (michaelpri10, Jacob-Gray and ProgramFOX) will check whether your code passes on Flake8 before it gets merged.
