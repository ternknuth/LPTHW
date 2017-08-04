#!/usr/bin/env python3

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi {0!s}, I'm the {1!s} script." . format(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me {0!s}?" . format(user_name))
likes = input(prompt)

print("Wheres do you live {0!s}?" . format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {0!r} about liking me.
You live in {1!r}.  Not sure where that is.
And you have a {2!r} computer.  Nice.\
""" . format(likes, lives, computer))
