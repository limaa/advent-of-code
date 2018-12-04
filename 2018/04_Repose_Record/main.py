#!/usr/bin/env python3

with open("input.txt", "r") as f:
    records = f.read().splitlines()

from datetime import datetime
from collections import defaultdict, Counter

def parseRecord(record):
    l = record.split()

    ymd = l[0].split("[")[1]
    hm = l[1].split("]")[0]
    year = int(ymd.split("-")[0])
    month = int(ymd.split("-")[1])
    day = int(ymd.split("-")[2])
    hour = int(hm.split(":")[0])
    minute = int(hm.split(":")[1])

    guardId = 0 if l[2] != "Guard" else int(l[3].split("#")[1])
    fallsAsleep = False if l[2] != "falls" else True
    wakesUp = not fallsAsleep if guardId == 0 else False

    r = {
        "datetime": datetime(year, month, day, hour, minute),
        "guardId": guardId,
        "fallsAsleep": fallsAsleep,
        "wakesUp": wakesUp
    }
    return r

def proccessRecords(records):
    rList = [parseRecord(r) for r in records]
    recordsList = sorted(rList, key=lambda k: k["datetime"])

    guardId = 0
    falls = datetime.now()
    wakes = datetime.now()
    totalSlept = defaultdict(int)
    minutesListing = defaultdict(list)
    for r in recordsList:
        if r["guardId"] != 0:
            guardId = r["guardId"]
            continue
        
        if r["fallsAsleep"]:
            falls = r["datetime"]
            continue
        
        if r["wakesUp"]:
            wakes = r["datetime"]
            totalSlept[guardId] += (wakes-falls).total_seconds()/60
            minutesListing[guardId] += range(falls.minute, wakes.minute)

    minutesListingSorted = {}
    for guardId, minutesList in minutesListing.items():
        minutesListingSorted[guardId] = Counter(minutesList).most_common()

    return [totalSlept, minutesListingSorted]

def part_one(records):
    totalSlept, minutesListing = proccessRecords(records)

    sleepyGuardId = 0
    sleepyGuardMinutes = 0
    for guardId, totalMinutes in totalSlept.items():
        if totalMinutes > sleepyGuardMinutes:
            sleepyGuardMinutes = totalMinutes
            sleepyGuardId = guardId

    mostCommonMinute, _ = minutesListing[sleepyGuardId][0]

    return sleepyGuardId*mostCommonMinute

def part_two(records):
    _, minutesListing = proccessRecords(records)

    biggestAmout = 0
    minuteChosen = 0
    guardIdChosen = 0
    for guardId, minutesList in minutesListing.items():
        (minute, amount) = minutesList[0]
        if amount > biggestAmout:
            biggestAmout = amount
            minuteChosen = minute
            guardIdChosen = guardId
    
    return guardIdChosen*minuteChosen


recordsExample = ["[1518-11-01 00:00] Guard #10 begins shift",
                "[1518-11-01 00:05] falls asleep", 
                "[1518-11-01 00:25] wakes up", 
                "[1518-11-01 00:30] falls asleep", 
                "[1518-11-01 00:55] wakes up", 
                "[1518-11-01 23:58] Guard #99 begins shift", 
                "[1518-11-02 00:40] falls asleep", 
                "[1518-11-02 00:50] wakes up", 
                "[1518-11-03 00:05] Guard #10 begins shift", 
                "[1518-11-03 00:24] falls asleep", 
                "[1518-11-03 00:29] wakes up", 
                "[1518-11-04 00:02] Guard #99 begins shift", 
                "[1518-11-04 00:36] falls asleep", 
                "[1518-11-04 00:46] wakes up", 
                "[1518-11-05 00:03] Guard #99 begins shift", 
                "[1518-11-05 00:45] falls asleep", 
                "[1518-11-05 00:55] wakes up"]

assert part_one(recordsExample) == 240
assert part_two(recordsExample) == 4455

print("Part one: %d" % part_one(records))
print("Part two: %s" % part_two(records))