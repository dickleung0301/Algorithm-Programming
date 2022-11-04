import sys

args = sys.argv

def check_int(index): # check is it an integer
    for i in range(len(args[index])):
        if (ord(args[index][i]) > 57) or (ord(args[index][i]) < 48):
            return True

if len(args) != 2: # check the no. of passing arg
    print(False)

if check_int(1):
    print(False)

for i in range(int(args[1])):
    if i % 2 == 0:
        print(' *'*int(args[1]))
    else:
        print('* '*int(args[1]))