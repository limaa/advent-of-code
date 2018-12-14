#!/usr/bin/env python3

with open("input.txt", "r") as f:
    steps = f.read().splitlines()

example = ["Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin."]

# steps = example
workers = 1
minStepTime = 0

# Assign children
stepsDict = {}
for s in steps:
    l = s.split()
    stepLetter = l[1]
    childLetter = l[7]

    if stepLetter in stepsDict.keys():
        stepsDict[stepLetter]["children"] += [childLetter]
    else:
        stepsDict[stepLetter] = {
            "currStep": stepLetter,
            "parents": [],
            "children": [childLetter]
        }

# Create last step
lastSteps = {}
for key, step in stepsDict.items():
    for child in step["children"]:
        if child not in stepsDict.keys():
            lastSteps[child] = {
                "currStep": child,
                "parents": [],
                "children": []
            }
stepsDict.update(lastSteps)

# Assign parents
for key,step in stepsDict.items():
    for childLetter in step["children"]:
        stepsDict[childLetter]["parents"] += [key]

def allParentStepsExecuted(step, executedSteps):
    allParentsExec = True
    for p in step["parents"]:
        if p not in executedSteps:
            allParentsExec = False
    return allParentsExec

firstSteps = []
for key, step in stepsDict.items():
    if step["parents"] == []:
        firstSteps.append(step.copy())
firstSteps = sorted(firstSteps, key=lambda step: step["currStep"])

orderOfExecution = ""
availableSteps = [s["currStep"] for s in firstSteps]
unavailableSteps = []
workersPool = [0]*workers
currStep = stepsDict[availableSteps.pop(0)]
while True:
    orderOfExecution += currStep["currStep"]

    # Distribute work among workers
    for w in workersPool:
        pass

    # Move unavailable to available
    for letter in unavailableSteps.copy():
        available = allParentStepsExecuted(stepsDict[letter], orderOfExecution)
        if available:
            availableSteps += letter
            unavailableSteps.remove(letter)

    for c in currStep["children"]:
        available = allParentStepsExecuted(stepsDict[c], orderOfExecution)
        if available and c not in availableSteps:
            availableSteps += c
        
        if not available and c not in unavailableSteps:
            unavailableSteps +=c

    if availableSteps == [] and currStep["children"] == []:
        break

    availableSteps.sort()
    currStep = stepsDict[availableSteps.pop(0)]

print(orderOfExecution)