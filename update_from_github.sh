#!/usr/bin/python

cd /opt/PPC_WB_Tester
#pip install --upgrade git+https://github.com/dehusky/PPCWaterBlock/*
#curl -v -H "Authorization:103d0193b48df2634e1612e6a566d68a791e5e67" https://api.github.com/dehusky/PPCWaterBlock

sudo git pull origin master
sh run.sh
