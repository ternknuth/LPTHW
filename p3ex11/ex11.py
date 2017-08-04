#!/usr/bin/env python3

print("How old are you? " , end = ''),
age = input()
print("How tall are you? " , end = '')
height = input()
print("How much do you weigh? " , end = '')
weight = input()

print("So, you're {0!r} old, {1!r} tall and {2!r} heavy." .format(age, height, weight))
