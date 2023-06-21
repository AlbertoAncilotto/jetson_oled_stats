#!/usr/bin/env python

from demo_opts import get_device
from luma.core.render import canvas
from time import sleep
import socket
import subprocess

def get_cpu_temperatures():
    """Returns the first two CPU temperature readings as floats."""
    # Run the command and split the output by lines
    output = subprocess.check_output("cat /sys/devices/virtual/thermal/thermal_zone*/temp", shell=True)
    lines = output.decode().split("\n")

    # Convert the first two lines to floats and return as a tuple
    cputemp = float(lines[0]) / 1000
    gputemp = float(lines[1]) / 1000
    return cputemp, gputemp

def get_ip_address():
    """Returns the IP address of the device."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    # print(ip_address)
    return ip_address

def main(device):
    # Get the IP address of the device
    while True:
        ip_address = get_ip_address()
        cputemp, gputemp = get_cpu_temperatures()

        # Clear the screen and show the IP address
        device.clear()
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((30, 10), ip_address, fill="white")
            draw.text((30, 40), f"CPU: {cputemp:.2f}°C, GPU: {gputemp:.2f}°C", fill="white")
        sleep(2)


if __name__ == "__main__":
    try:
        device = get_device()
        main(device)
    except KeyboardInterrupt:
        pass
