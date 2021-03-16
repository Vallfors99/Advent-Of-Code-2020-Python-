import sys
from copy import deepcopy
input_file = sys.stdin
input_file = open("input.txt", 'r')


def isEquation(elem_1, elem_2, elem_3):
    # Check if 3 consecutive elements form a valid equation alt. contain unnessesary parentheses
    cond1 = elem_1.isnumeric and elem_1 not in "()"
    cond2 = elem_2 in operators
    cond3 = elem_3.isnumeric and elem_3 not in "()"
    if all([cond1, cond2, cond3]):
        return 1
    elif elem_1 == "(" and elem_3 == ")":
        return 2
    else:
        return 0


lines = input_file.readlines()
lines = [[elem for elem in line.strip().replace(" ", "")] for line in lines]
lines_backup = deepcopy(lines)
operators = ("+", "*")  # these are all valid operators
res = []

for part in (1, 2):  # part 1: left to right priority, part 2: L->R & "+" priority
    for line in lines:
        i = 0
        while len(line) > 1:

            first, middle, third = str(line[i]), str(line[i+1]), str(line[i+2])
            analysis = isEquation(first, middle, third)
            endOfLine = (i+3) > (len(line)-1)

            # if the 3 elements form an equation of priority:
            # replace the 3 elements with one element containing value of equation
            if analysis == 1 and (part == 1 or (middle == "+" or endOfLine or line[i+3] != "+")):
                line[i] = eval(f'{first} {middle} {third}')
                line = line[0:i+1] + line[i+3:]
                i = 0

            # remove unnecessary parentheses if any; "(123)" --> "123"
            elif analysis == 2:
                line = line[0:i] + \
                    line[i+1:i+2] + line[i+3:]
                i = 0

            else:
                i += 1
        res.append(int(line[0]))
    lines = lines_backup  # getting the old lines back

    print(f'part{part}: the sum of all lines is equal to {sum(res)}')
    res = []

input_file.close()
