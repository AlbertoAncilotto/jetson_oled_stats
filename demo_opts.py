# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# Copyright (c) 2022 SMARTCOW AI TECHNOLOGIES LTD

import sys
import logging

from luma.core import cmdline, error

import Jetson.GPIO as GPIO
GPIO.setwarnings(False)

#DEVICE = "SSD1362"
DEVICE = "SH1122"

if DEVICE == "SSD1362":
    apollo_args = ['--spi-port', '2', '--spi-device', '0', '--interface', 'spi', '--gpio', 'Jetson.GPIO', '--gpio-mode', 'Jetson.GPIO.BOARD', '--gpio-data-command', '32', '--gpio-reset', '31', '--gpio-reset-hold-time', '0.1']
    apollo_config = ['--display=ssd1362', '--width=256', '--height=64', '--spi-bus-speed=2000000']
elif DEVICE == "SH1122":
    apollo_args = ['--spi-port', '2', '--spi-device', '0', '--interface', 'spi', '--gpio', 'Jetson.GPIO', '--gpio-mode', 'Jetson.GPIO.BOARD', '--gpio-data-command', '32', '--gpio-reset', '31', '--gpio-reset-hold-time', '0.1']
    apollo_config = ['--display=sh1122', '--width=256', '--height=64', '--spi-bus-speed=2000000']


# logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s - %(message)s'
)
# ignore PIL debug messages
logging.getLogger('PIL').setLevel(logging.ERROR)


def display_settings(device, args):
    """
    Display a short summary of the settings.

    :rtype: str
    """
    iface = ''
    display_types = cmdline.get_display_types()
    if args.display not in display_types['emulator']:
        iface = 'Interface: {}\n'.format(args.interface)

    lib_name = cmdline.get_library_for_display_type(args.display)
    if lib_name is not None:
        lib_version = cmdline.get_library_version(lib_name)
    else:
        lib_name = lib_version = 'unknown'

    import luma.core
    version = 'luma.{} {} (luma.core {})'.format(
        lib_name, lib_version, luma.core.__version__)

    return 'Version: {}\nDisplay: {}\n{}Dimensions: {} x {}\n{}'.format(
        version, args.display, iface, device.width, device.height, '-' * 60)


def get_device(actual_args=apollo_args):
    """
    Create device from command-line arguments and return it.
    """
    if actual_args is None:
        actual_args = sys.argv[1:]
    
    parser = cmdline.create_parser(description='luma.examples arguments')
    args = parser.parse_args(apollo_config + actual_args)

    # create device
    try:
        device = cmdline.create_device(args)
        return device

    except error.Error as e:
        parser.error(e)
        return None
