import sys
import re
input_file = sys.stdin


if len(sys.argv) > 1:
    input_file = open(sys.argv[1], 'r')
    lines = input_file.readlines()
    lines[0] = lines[0].strip()
    lines[1] = lines[1].split(",")
    lines[1] = [int(number) for number in lines[1] if number != "x"]

    # solution

    modlist = [int(lines[0]) % int(number) for number in lines[1]]
    waitlist = [lines[1][i] - modlist[i] for i in range(0, len(lines[1]))]
    index_min = min(range(len(waitlist)), key=waitlist.__getitem__)
    busID = lines[1][index_min]
    waitTime = waitlist[index_min]

    print(f"ans: {waitTime*busID}")
    input_file.close()
