#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else ((-number % 10) * -1)
message = f"Last digit of {number} is {last_digit}"
