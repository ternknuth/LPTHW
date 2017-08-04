#!/usr/bin/env python3

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {0!s} to {1!s}" .format(from_file, to_file))

# We could do these two on one line too, how?
inputfile = open(from_file)    # python3中使用input()为输入函数，因此变量名不能再用input。
indata = inputfile.read()

print("The input file is {0} bytes long" .format(len(indata)))

print("Does the output file exist? {0!r}" .format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

output = open(to_file, 'w')
output.write(indata)

print("Alright. all done.")

output.close()
inputfile.close()
