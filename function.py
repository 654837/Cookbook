#!/usr/bin/env python3

def greetUser():
  """Generic greeting for users"""
  print("Hello!")
  print("Welcome")


def greetUserByName(name="user", greeting="Hello"):
  """Customized greeting"""
  print(greeting + ", " + name)


def cube(baseNumber):
  cubedValue = baseNumber * baseNumber * baseNumber
  return cubedValue


greetUser()
greetUserByName(input("What is your name? "))
greetUserByName()
greetUserByName(input("What is your name? "), "Welcome")
greetUserByName(greeting="Welcome", name="NanoDano")

elevenCubed = cube(11)
print(elevenCubed)

