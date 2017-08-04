#!/usr/bin/env python3

formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I hand thie thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

print('-' * 60)

formatter = "{0} {1} {2} {3}"

print(formatter .format(1, 2, 3, 4))
print(formatter .format(repr("one"), repr("two"), repr("three"), repr("four")))
print(formatter .format(repr(True), repr(False), False, True))
print(formatter .format(repr(formatter), repr(formatter), repr(formatter), repr(formatter)))
print(formatter .format(
    repr("I hand thie thing."),
    repr("That you could type up right."),
    repr("But it didn't sing."),
    repr("So I said goodnight.")
))

print('-' * 60)

formatter = "{0!r} {1!r} {2!r} {3!r}"

print(formatter .format(1, 2, 3, 4))
print(formatter .format("one", "two", "three", "four"))
print(formatter .format(True, False, False, True))
print(formatter .format(formatter, formatter, formatter, formatter))
print(formatter .format(
    "I hand thie thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
