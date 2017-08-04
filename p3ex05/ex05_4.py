#!/usr/bin/env python3

name = "Zed A. Shaw"
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# 1英寸(in)=2.54厘米(cm)
in_to_cm_rate = 2.54
height_cm = height * in_to_cm_rate
# 1磅(lb)=0.4535924千克(kg)
lb_to_kg_rate = 0.4535924
weight_kg = weight * lb_to_kg_rate


print("Let's talk about {0}." .format(name))
print("He's {0} cm tall." .format(height_cm))
print("He's {0} kg heavy." .format(weight_kg))
print("Actually that's not too heavy.")
print("He's got '{0}' eyes and {1} hair." .format(eyes, hair))
print("His teeth are usually {0} depending on the coffee." .format(teeth))

# this line is tricky, rty to get it exactly right
print("If I add {0}, {1}, and {2} I get {3}." .format(age, height_cm, weight_kg, age + height_cm + weight_kg))
