import sys
import re
input_file = sys.stdin

if len(sys.argv) > 1:
    input_file = open(sys.argv[1], 'r')
    k = input_file.readlines()
    lines = k[1]
    lines = lines.split(",")
    buslist = []
    rests = []
    for i in range(0, len(lines)):
        if lines[i] == "x":
            continue
        else:
            buslist.append(int(lines[i]))
            rests.append(i)
    t = 0
    check = 0

addval = buslist[0]
x = 1
while x < len(buslist):
    while check == 0:
        printlist = [(t + rests[x]) % buslist[x]
                     for x in range(0, len(buslist))]

        if printlist[x] == 0:
            addval = addval*buslist[x]
            x += 1
        if max(printlist) == 0:
            print(t)
            check = 1
        t += addval
