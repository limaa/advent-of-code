#!/usr/bin/env python3

import numpy as np
from collections import Counter
import time

def proccessInputList(inputList):
    return [np.array(list(map(int, c.split(',')))) for c in inputList]

with open("input.txt", "r") as f:
    proccessedInput = proccessInputList(f.read().splitlines())

def processCoordinates(coordinates, safeDistance = 32):
    xMin, xMax = [min([c[0] for c in coordinates]), max([c[0] for c in coordinates])]
    yMin, yMax = [min([c[1] for c in coordinates]), max([c[1] for c in coordinates])]

    safeArea = 0
    areaCnt = len(coordinates)*[0]
    isInfinite = len(coordinates)*[False]
    for y in range(yMin, yMax+1):
        yDists = np.array([abs(c[1]-y) for c in coordinates])

        for x in range(xMin, xMax+1):
            xDists = np.array([abs(c[0]-x) for c in coordinates])
            dists = xDists+yDists
            smallestDist = min(dists)

            if Counter(dists)[smallestDist] == 1:
                idx = np.where(dists == smallestDist)[0][0]
                areaCnt[idx] += 1
                if x in [xMin, xMax] or y in [yMin, yMax]:
                    isInfinite[idx] = True

            if sum(dists) < safeDistance:
                safeArea += 1

    return areaCnt, isInfinite, safeArea

def test(coordinates, safeDistance = 32):
    xMin, xMax = [min([c[0] for c in coordinates]), max([c[0] for c in coordinates])]
    yMin, yMax = [min([c[1] for c in coordinates]), max([c[1] for c in coordinates])]
    xRange = range(xMin, xMax+1)
    yRange = range(yMin, yMax+1)
    numPixelsX = len(xRange)
    numPixelsY = len(yRange)
    numPixels = numPixelsX*numPixelsY

    safeArea = 0
    areaCnt = len(coordinates)*[0]
    isInfinite = len(coordinates)*[False]
    xDists = np.array([np.array([abs(c[0]-x) for c in coordinates]) for x in xRange])
    yDists = np.array([np.array([abs(c[1]-y) for c in coordinates]) for y in yRange])
    distances = (xDists.repeat(numPixelsY, axis=0) + np.concatenate((yDists,)*numPixelsX))
    safeArea = np.sum(distances.sum(axis=1) < safeDistance)

    smallestDistance = distances.min(axis=1).reshape(numPixels, 1)
    pixelsToKeep = (np.sum(distances == smallestDistance,axis=1) == 1)
    testSmallDistancesRemoved = smallestDistance[pixelsToKeep]
    testLinesRemoved = distances[pixelsToKeep]
    testWhere = np.where(testSmallDistancesRemoved == testLinesRemoved)
    uniq, cnt = np.unique(testWhere, return_counts=True)
    testSum = list(zip(uniq, cnt))

    dists = {}
    smallestDist = {}
    for i in range(len(xRange)):
        x = xRange[i]
        for j in range(len(yRange)):
            y = yRange[j]
            dists[(x, y)] = xDists[i]+yDists[j]
            smallestDist[(x,y)] = min(dists[(x, y)])

            if Counter(dists[(x, y)])[smallestDist[(x,y)]] == 1:
                idx = np.where(dists[(x, y)] == smallestDist[(x,y)])[0][0]
                areaCnt[idx] += 1
                if x in [xMin, xMax] or y in [yMin, yMax]:
                    isInfinite[idx] = True

    return areaCnt, isInfinite, safeArea

def p1(areaCnt, isInfinite):
    return max([area if not isInf else 0 for area,isInf in zip(areaCnt, isInfinite)])

example = ["1, 1",
            "1, 6",
            "8, 3",
            "3, 4",
            "5, 5",
            "8, 9"]

t1 = time.time_ns()
areaCnt, isInfinite, safeArea = test(proccessInputList(example))
t2 = time.time_ns()
print(t2-t1)
assert p1(areaCnt, isInfinite) == 17
assert safeArea == 16

t1 = time.time_ns()
areaCnt, isInfinite, safeArea = processCoordinates(proccessInputList(example))
t2 = time.time_ns()
print(t2-t1)

assert p1(areaCnt, isInfinite) == 17
assert safeArea == 16

areaCnt, isInfinite, safeArea = processCoordinates(proccessedInput, 10000)
print("Part one: %d" % p1(areaCnt, isInfinite))
print("Part two: %d" % safeArea)
