#!/usr/bin/env python3
import os
import sys
import socket
import psutil

def check_reboot():
    return os.path.exists("/run/reboot-required")

def check_root_full():
    ''' Return True'''
    return check_disk_full()

def check_if_everything_true():
    return True

def check_no_network():
    '''return true if it fails to resolve google's url'''
    try:
        socket.gethostname('www.google.com')
        return False
    Except:
        return True

def main():
    checks = [(check_reboot(), 'pending reboot'),
              (check_root_full(), 'root partition full'),]
              (check_no_network(), 'no internet connection')]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if everything_ok:
      sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
