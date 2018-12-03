#!/usr/bin/env python3

with open("input.txt", "r") as f:
    claims = f.read().splitlines()

def parseClaim(claim):
    l = claim.split()
    c = {
        "identification": int(l[0].split("#")[1]),
        "x": int(l[2].split(",")[0]),
        "y": int(l[2].split(",")[1].split(":")[0]),
        "width": int(l[3].split("x")[0]),
        "height": int(l[3].split("x")[1])
    }
    return c

def part_one(claims):
    claimList = [parseClaim(c) for c in claims]

    import collections
    fabric = collections.defaultdict(int)
    for claim in claimList:
        for i in range(claim["x"], claim["x"] + claim["width"]):
            for j in range(claim["y"], claim["y"] + claim["height"]):
                fabric[(i, j)] += 1

    cnt = 0
    for val in fabric.values():
        if val > 1:
            cnt += 1
    return cnt

def part_two(claims):

    claimList = [parseClaim(c) for c in claims]
    
    import collections
    conflicts = collections.defaultdict(list)
    for c in claimList:
        for c2 in claimList:
            if c == c2:
                continue
            if (c["x"] < c2["x"]+c2["width"] and
                c["x"]+c["width"] > c2["x"] and
                c["y"] < c2["y"]+c2["height"] and
                c["y"]+c["height"] > c2["y"]):
                conflicts[c["identification"]] += [c2["identification"]]
    
    ret = 0
    idList = [c["identification"] for c in claimList]
    for i in idList:
        if i not in conflicts.keys():
            ret = i
    return ret


claimsExample = ["#1 @ 1,3: 4x4",
                "#2 @ 3,1: 4x4",
                "#3 @ 5,5: 2x2"]

assert part_one(claimsExample) == 4
assert part_two(claimsExample) == 3

print("Part one: %d" % part_one(claims))
print("Part two: %s" % part_two(claims))