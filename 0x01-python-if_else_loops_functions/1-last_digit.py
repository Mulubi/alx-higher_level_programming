#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastNum = int(repr(number)[-1])
#Followed by if the last digit of the number is greater than 5: "and is greater than 5"
if (LastNum > 5):
    print("Last digit of", "{:d}".format(number), "is", "{:d}".format(LastNum), "and is greater than 5")
#if the last digit is 0: "and is 0"
elif (LastNum == 0):
    print("Last digit of", "{:d}".format(number), "is", "{:d}".format(LastNum), "and is 0")
#if the last digit is less than 6 and not 0: "and is less than 6 and not 0"
else:
    print("Last digit of", "{:d}".format(number), "is", "{:d}".format(LastNum), "and is less than 6 and not 0")

#Should print something like this:
#Last digit of 4205 is 5 and is less than 6 and not 0
