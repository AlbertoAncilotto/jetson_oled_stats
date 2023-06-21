#!/bin/bash

# Get the path to the current directory
cwd=$(pwd)

# Add a cron job to run the Python script at boot time
(crontab -l ; echo "@reboot sleep 50 && /usr/bin/python3 $cwd/show_ip_temp.py >> $cwd/cron.log 2>&1") | crontab -