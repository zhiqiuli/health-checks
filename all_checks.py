#!/usr/bin/env python3
import os
import sys

def check_reboot():
    return os.path.exists("/run/reboot-required")

def check_root_full():
    ''' Return True'''
    return check_disk_full()

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_root_full():
        print("check if root space is available")    
    print("Another statement says everything here is OK.")
    print("Everything ok.")
    print("Yes - everything is ok.")
    sys.exit(0)

main()
