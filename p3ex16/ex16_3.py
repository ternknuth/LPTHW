#!/usr/bin/env python3

from sys import argv

script, filename = argv

print("We're going to erase {0!r}." .format(filename))
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Openning the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to writer these to the file.")

target.write("{0}\n{1}\n{2}\n" . format(line1, line2, line3))

print("And finally, we close it.")
target.close()
