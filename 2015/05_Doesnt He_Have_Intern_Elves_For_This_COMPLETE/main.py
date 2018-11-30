#!/usr/bin/env python3

with open("input.txt", "r") as f:
    strList = f.read().splitlines()

def part1(strList):
    msgCount = 0
    for msg in strList:
        if "ab" in msg:
            continue

        if "cd" in msg:
            continue

        if "pq" in msg:
            continue

        if "xy" in msg:
            continue

        cntVowels = 0
        hasDoubleLetter = False
        for i in range(len(msg)):
            if i != len(msg)-1:
                if msg[i] == msg[(i+1)]:
                    hasDoubleLetter = True
            
            if "a" == msg[i] or \
            "e" == msg[i] or \
            "i" == msg[i] or \
            "o" == msg[i] or \
            "u" == msg[i]:
                cntVowels += 1

            if cntVowels >= 3 and hasDoubleLetter:
                break
        
        if cntVowels >= 3 and hasDoubleLetter:
            msgCount += 1
        
    return msgCount


def part2(strList):
    msgCount = 0
    for msg in strList:
        foundPair = False
        hasRepeatedLetter = False
        for i in range(len(msg)-2):
            if not hasRepeatedLetter and msg[i] == msg[(i+2)]:
                hasRepeatedLetter = True
            
            if not foundPair and msg[i:i+2] in msg[i+2:]:
                foundPair = True

            if foundPair and hasRepeatedLetter:
                break
        
        if foundPair and hasRepeatedLetter:
            msgCount += 1
    return msgCount

print(part2(strList))