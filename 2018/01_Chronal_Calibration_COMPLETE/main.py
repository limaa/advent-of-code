#!/usr/bin/env python3

with open("input.txt", "r") as f:
    freqs = f.read().splitlines()

# freqs = ["+1", "-2", "+3", "+1"] # Result: 3
# freqs = ["+1", "+1", "+1"] # Result: 3
# freqs = ["+1", "+1", "-2"] # Result 0
# freqs = ["-1", "-2", "-3"] # Result: -6
currFreq = 0
freqsReached = {
    0: 1
}
foundFreqReachedTwice = False
while(not foundFreqReachedTwice):
    for i in range(len(freqs)):
        freq = int(freqs[i])
        # print("Current frequency: %d \tchange: %d \tresulting freq: %d" % (currFreq, freq, (currFreq+freq)))

        currFreq += freq
        if currFreq in freqsReached.keys():
            print("Frequency %d reached twice!" % currFreq)
            freqsReached[currFreq] += 1
            foundFreqReachedTwice = True
            break
        else:
            freqsReached[currFreq] = 1

print("Current frequency: %d" % currFreq)