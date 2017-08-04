#!/usr/bin/env python3

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

# 20以内的基数词转序数词可用此简单办法
for i in range(0, len(animals)):
    if i+1 == 1:
        print("The {0}st " . format(i+1), end="")
    elif i + 1 == 2:
        print("The {0}nd " . format(i+1), end="")
    elif i + 1 == 3:
        print("The {0}rd " . format(i+1), end="")
    else:
        print("The {0}th " . format(i+1), end="")
    print("animal is at {0} and is a {1}." . format(i, animals[i]))

print("\n----------\n")
    
for i in range(0, len(animals)):
    print("The animal at {0} is the " . format(i), end="")
    if i+1 == 1:
        print("{0}st " . format(i+1), end="")
    elif i + 1 == 2:
        print("{0}nd " . format(i+1), end="")
    elif i + 1 == 3:
        print("{0}rd " . format(i+1), end="")
    else:
        print("{0}th " . format(i+1), end="")
    print("animal and is a {0}." . format(animals[i]))
    
