#!/usr/bin/env python3

def append_list(my_numbers, my_range, my_step):
    i = 0
    while i < my_range:
        print("At the top i is {0}" .format(i))
        my_numbers.append(i)
        i = i + my_step
        print("Numbers now: ", my_numbers)
        print("At the bottom i is {0}" .format(i))

numbers = []
value_range = input("Please input a range number: ")
value_step = input("Please input a step number: ")

# input()的输入值，须用int()函数将字符串转为整数
append_list(numbers, int(value_range), int(value_step))   
        
print("The numbers: ")
for num in numbers:
    print(num)
