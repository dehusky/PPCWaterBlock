#!/bin/sh

if [ ! -d "/opt/PPCWaterBlock" ]
then
   sudo mkdir /opt/PPCWaterBlock
   echo "Directory created"
else
   echo "Directory exists, updating files..." 
fi

# copy all files from installation directory to local directory
cp -avr * /opt/PPCWaterBlock >> /tmp/PPC_WB_Tester_1.log 2>&1
echo "Files copied to /opt/PPCWaterBlock"

# copy run.sh
cp run.sh /usr/local/bin/run.sh >> /tmp/PPC_WB_Tester_2.log 2>&1
echo "Script run.sh copied to /usr/local/bin"
# make run.sh executable
sudo chmod ugo+x /usr/local/bin/run.sh


# check if autostart contains run.sh and if not add it
if (grep "$@/usr/local/bin/run.sh" /etc/xdg/lxsession/LXDE-pi > /dev/null)
then
   echo "run.sh found in /lxsession/autostart"
else
   # echo "lxsession/autostart checked, run.sh not found, adding now..."
   echo "@/opt/PPCWaterBlock/run.sh" >> /etc/xdg/lxsession/LXDE-pi/autostart
   echo "added run.sh routine to lxsession/autostart"
fi
