#!/usr/bin/env python3

with open("input.txt", "r") as f:
    msgs = f.read().splitlines()

def part_one(msgs):
    import collections

    twices = 0
    thrices = 0
    for msg in msgs:
        d = collections.defaultdict(int)
        for c in msg:
            d[c] += 1
        
        if 2 in d.values():
            twices += 1
        if 3 in d.values():
            thrices += 1

    # print("Twices: %d" % twices)
    # print("Thrices: %d" % thrices)
    # print("Result: %d" % (twices*thrices))
    return twices*thrices

def part_two(msgs):
    def hamming_distance(s1, s2):
        assert len(s1) == len(s2)
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    for i in range(len(msgs)):
        for j in range(i+1, len(msgs)):
            hd = hamming_distance(msgs[i], msgs[j])
            if hd == 1:
                res = ""
                for ch1, ch2 in zip(msgs[i], msgs[j]):
                    if ch1 == ch2:
                        res += ch1
                # print("Found boxes")
                # print("ID: %s\tID: %s" % (msgs[i], msgs[j]))
                # print("Result: %s" % res)
                return res
            # print("Hamming Distance: %d\tM1: %s\tM2: %s" % (hd, msgs[i], msgs[j]))


msgs1 = ["abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab"]

msgs2 = ["abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz"]

assert part_one(msgs1) == 12
assert part_two(msgs2) == "fgij"

print("Part one: %d" % part_one(msgs))
print("Part two: %s" % part_two(msgs))