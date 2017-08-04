#!/usr/bin/env python3

from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file {0!r}:" . format(filename))
print(txt.read())
txt.close()     # 及时关闭打开的文件

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# 及时关闭打开的文件
txt_again.close()
