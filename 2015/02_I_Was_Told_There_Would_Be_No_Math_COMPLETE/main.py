#!/usr/bin/env python3

with open("input.txt", "r") as f:
    dimensionsList = f.read().splitlines()

# print(dimensionsList)
# dimensionsList = ["2x3x4"]
wrappingPaper = 0
ribbon = 0
for dim in dimensionsList:
    [l, w, h] = [int(s) for s in dim.split("x")]
    # print("l: %d w: %d h: %d" % (l, w, h))

    areas = [l*w, l*h, w*h]
    surfaceArea = sum(2*areas)+min(areas)
    wrappingPaper += surfaceArea

    perimeters = [2*(l+w), 2*(l+h), 2*(w+h)]
    wrappingRibbon = min(perimeters)
    bowRibbon = l*w*h
    ribbon += wrappingRibbon + bowRibbon


print("Wrapping paper: %d" % wrappingPaper)
print("Ribbon: %d" % ribbon)
