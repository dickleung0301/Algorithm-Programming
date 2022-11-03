import sys

args = sys.argv
length = len(args)
index = length - 1
output = ''
for i in range(length - 1):
    iteration = ' ' + args[index] + ','
    output += iteration
    index -= 1
output = output.rstrip(output[-1])
print('Hi' + output)