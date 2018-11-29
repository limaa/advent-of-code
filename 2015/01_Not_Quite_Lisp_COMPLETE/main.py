#!/usr/bin/env python3

with open("input.txt", "r") as f:
    inputTxt = "".join(f.read().splitlines())

santaWasInBasement = False
floor = 0
for i in range(len(inputTxt)):
    if inputTxt[i] == "(":
        floor += 1
    else:
        floor -= 1
    
    if floor < 0 and not santaWasInBasement:
        print("Santa entered the basement: %d" % (i+1))
        santaWasInBasement = True

print(floor)

