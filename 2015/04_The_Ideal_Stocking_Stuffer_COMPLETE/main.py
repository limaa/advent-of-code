#!/usr/bin/env python3

import hashlib
import struct

with open("input.txt", "r") as f:
    inputKey = ''.join(f.read().splitlines())

# inputKey = "abcdef"

num = 0
keyFound = False
while not keyFound:
    num += 1

    if num % 100000 == 0:
        print("Trying: %d" % num)

    key = inputKey + str(num)
    m = hashlib.md5(key.encode()).digest()
    a, b, c = struct.unpack('3B', m[0:3])

    if (a == 0 and b == 0 and c == 0): # c < 8):
        print("    Found number: %d" % num)
        keyFound = True