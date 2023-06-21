# Jetson IP/Temp Display
This Python script displays the current IP address and CPU/GPU temperatures on an OLED display connected to a NVIDIA Jetson board. The script uses the luma.oled library to communicate with the OLED display and the subprocess module to read the CPU/GPU temperatures from the system.

# Prerequisites
NVIDIA Jetson board
OLED display compatible with the luma.oled library
Python 3
luma.oled Python library

# Installation
To install and run the jetson_ip_temp_display script at startup:

Clone this repository to your Jetson board.
Copy
git clone https://github.com/your-username/jetson-ip-temp-display.git
Run the install.sh script as root to add a cron job that automatically starts the display after one minute from startup.
```
chmod +x install.sh
./install.sh
```

Reboot the Jetson board to start the display.
```
sudo reboot
```

# Usage
The show_ip_temp.py script displays the current IP address and CPU/GPU temperatures on the OLED display. To run the script manually, run the following command:

```
python3 show_ip_temp.py
```

The script will continuously update the display with the current IP address and CPU/GPU temperatures.

# Contributing
If you find any bugs or have suggestions for improving the script, please open an issue or submit a pull request on GitHub.