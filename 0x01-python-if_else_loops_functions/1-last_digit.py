#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new_number = (-1) * number
    last_number = new_number % 10
    last_number = (-1) * last_number
else:
    last_number = number % 10
if last_number > 5:
    print("Last digit of {} is {} and is greater than 5".format
          (number, last_number))
elif last_number < 6 and last_number != 0:
    if last_number < 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format
              (number, last_number))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format
              (number, last_number))
else:
    print("Last digit of {} is {} and is 0".format(number, last_number))
