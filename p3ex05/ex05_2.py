#!/usr/bin/env python3

name = "Zed A. Shaw"
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about {0}." .format(name))
print("He's {0} inches tall." .format(height))
print("He's {0} pounds heavy." .format(weight))
print("Actually that's not too heavy.")
print("He's got '{0}' eyes and {1} hair." .format(eyes, hair))
print("His teeth are usually {0} depending on the coffee." .format(teeth))

# this line is tricky, rty to get it exactly right
print("If I add {0}, {1}, and {2} I get {3}." .format(age, height, weight, age + height + weight))
