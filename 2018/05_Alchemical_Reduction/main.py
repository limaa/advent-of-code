#!/usr/bin/env python3

with open("input.txt", "r") as f:
    polymer = "".join(f.read().splitlines())

def proccessPoly(polymer):
    res = []
    for i in range(len(polymer)):
        res += [polymer[i]]
        if len(res) > 1 and res[-2] == res[-1].swapcase():
            res[-2:] = []
    return "".join(res)

def p1(polymer):
    return len(polymer)

def p2(polymer):
    return min(map(lambda letter: len(proccessPoly(polymer.replace(letter, "").replace(letter.swapcase(), ""))), "abcdefghijklmnopqrstuvwxyz"))

polymerExample = "dabAcCaCBAcCcaDA"
processedPoly = proccessPoly(polymerExample)
assert p1(processedPoly) == 10
assert p2(processedPoly) == 4

processedPoly = proccessPoly(polymer)
print("Part one: %d" % p1(processedPoly))
print("Part two: %d" % p2(processedPoly))
