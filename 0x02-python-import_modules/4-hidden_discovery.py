#!/usr/bin/python3
# 4-hidden_discovery.py
import sys
import hidden_4 as hidden
if __name__ != "__main__":
    exit()

name = dir(hidden)
for name in names:
        if name[:2] != "__":
            print(name)
