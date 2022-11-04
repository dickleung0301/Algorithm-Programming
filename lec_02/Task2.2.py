import sys

args = sys.argv

def check_str(index): # check str first or flow into other check will ereor
    if len(args[index]) < 3:
        return True
    elif ord(args[index][0]) >= 48 and ord(args[index][0]) <= 57 and args[index][1] == '.':
        temp = args[index][2:]
        for i in range(len(temp)):
            if (ord(temp[i]) > 57) or (ord(temp[i]) < 48):
                return True
    else:
        return True

def Task2_2(args):
    if check_str(1):
        print(False)
        return
    if check_str(2):
        print(False)
        return
    if len(args) != 3:
        print(False)
    elif (float(args[1]) >= 0) and (float(args[1]) <= 1) and (float(args[2]) >= 0) and (float(args[2]) <= 1):
        print(True)
    else:
        print(False)

Task2_2(args)