#!/usr/bin/env python3

print("The result of 'True and True' is True.  \t\t\t1. ", True and True)
print("The result of 'False and True' is False.  \t\t\t2. ", False and True)
print("The result of '1 == 1 and 2 == 1' is False. \t\t\t3. ", 1 == 1 and 2 == 1)
print("The result of '\"test\" == \"test\"' is True. \t\t\t4. ", "test" == "test")
print("The result of '1 == 1 or 2 != 1' is True. \t\t\t5. ", 1 == 1 or 2 != 1)

print("The result of 'True and 1 == 1' is True. \t\t\t6. ", True and 1 == 1)
print("The result of 'False and 0 != 0' is False. \t\t\t7. ", False and 0 != 0)
print("The result of 'True or 1 == 1' is True. \t\t\t8. ", True or 1 == 1)
print("The result of '\"test\" != \"testing\"' is True. \t\t\t9. ", "test" != "testing")
print("The result of '1 != 0 and 2 == 1' is False. \t\t\t10. ", 1 != 0 and 2 == 1)

print("The result of '\"test\" != \"testing\"' is True. \t\t\t11. ", "test" != "testing")
print("The result of '\"test\" == 1' is False. \t\t\t\t12. ", "test" == 1)
print("The result of 'not (True and False)' is True. \t\t\t13. ", not (True and False))
print("The result of 'not (1 == 1 and 0 != 1)' is False. \t\t14. ", not (1 == 1 and 0 != 1))
print("The result of 'not (10 == 1 or 1000 == 1000)' is False. \t15. ", not (10 == 1 or 1000 == 1000))

print("The result of 'not (1 != 10 or 3 == 4)' is False. \t\t16. ", not (1 != 10 or 3 == 4))
print("The result of 'not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\")' is True. \t\t17. ", not ("testing" == "testing" and "Zed" == "Cool Guy"))
print("The result of '1 == 1 and not (\"testing\" == 1 or 1 == 0)' is True. \t\t\t18. ", 1 == 1 and not ("testing" == 1 or 1 == 0))
print("The result of '\"chunky\" == \"bacon\" and not (3 == 4 or 3 == 3)' is False. \t\t19. ", "chunky" == "bacon" and not (3 == 4 or 3 == 3))
print("The result of '3 == 3 and not (\"testing\" == \"testing\" or \"Python\" == \"Fun\")' is False. \t20. ", 3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))
