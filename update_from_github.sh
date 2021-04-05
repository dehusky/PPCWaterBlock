#!/usr/bin/python

cd /opt/PPCWaterBlock

sudo git pull origin master

FILE=/home/pi/Desktop/WaterBlockTimer
if test -f "$FILE"; then
    echo "$FILE exists."
else
    sudo cp /opt/PPCWaterBlock/WaterBlockTimer /home/pi/Desktop/
    echo "$FILE added to desktop."
fi

sh run.sh
