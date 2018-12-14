#!/usr/bin/env python3

with open("input.txt", "r") as f:
    numbers = list(map(int, "".join(f.read().splitlines()).split()))

# example = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
# numbers = list(map(int, example.split()))

def processNode(numbers):
    metaData = []
    pos = 2
    value = 0

    childCount = numbers[0]
    metaDataCount = numbers[1]

    if (childCount == 0):
        metaData = numbers[2:2+metaDataCount]
        pos += metaDataCount
        value = sum(metaData)
    else:       
        pos = 2
        childValue = {}
        for i in range(childCount):
            tags, buffPos, childValue[i+1] = processNode(numbers[pos:])
            pos += buffPos
            metaData += tags
        nodeMetaData = numbers[pos:pos+metaDataCount]
        metaData += nodeMetaData
        pos += metaDataCount

        for idx in nodeMetaData:
            if idx in childValue.keys():
                value += childValue[idx]

    return [metaData, pos, value]

# print(processNode(numbers))
metaData, _, value = processNode(numbers)
print("Root node value: %d" % value)
print("Metadata sum: %d" % sum(metaData))