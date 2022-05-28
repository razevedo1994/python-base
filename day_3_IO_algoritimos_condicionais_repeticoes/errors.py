#!/usr/bin/env python3

import sys
import os

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")


try:
    print(names[2])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)
