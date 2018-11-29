#!/usr/bin/env python3

with open("input.txt", "r") as f:
    directions = ''.join(f.read().splitlines())

santaMap = {(0,0): 1}
robotMap = {(0,0): 1}
santaX = 0
santaY = 0
robotX = 0
robotY = 0
santaTurn = True
for direction in directions:
    if santaTurn:
        x = santaX
        y = santaY
    else:
        x = robotX
        y = robotY

    if direction == "^":
        y += 1
    elif direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    elif direction == "v":
        y -= 1

    if santaTurn:
        if (x,y) in santaMap.keys():
            santaMap[(x,y)] += 1
        else:
            santaMap[(x,y)] = 1
        santaTurn = False
        santaX = x
        santaY = y
    else:
        if (x,y) in robotMap.keys():
            robotMap[(x,y)] += 1
        else:
            robotMap[(x,y)] = 1
        santaTurn = True
        robotX = x
        robotY = y

mergedMap = {**santaMap, **robotMap}
print(len(mergedMap.keys()))
