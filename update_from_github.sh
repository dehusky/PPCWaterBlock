#!/usr/bin/python

import git

cd /opt/PPC_WB_Tester
g=git.cmd.Git('https://github.com/dehusky/PPCWaterBlock')

g.pull()
#sudo git pull origin master
