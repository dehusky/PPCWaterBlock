#!/usr/bin/python

cd /opt/PPC_WB_Tester
#pip install --upgrade git+https://github.com/dehusky/PPCWaterBlock/*
#curl -v -H "Authorization:103d0193b48df2634e1612e6a566d68a791e5e67" https://api.github.com/dehusky/PPCWaterBlock

sudo git pull origin master

FILE=/home/pi/Desktop/WaterBlockTimer
if test -f "$FILE"; then
    echo "$FILE exists."
else
    sudo cp /opt/PPCWaterBlock/Water Block Timer /home/pi/Desktop/
fi

sh run.sh
