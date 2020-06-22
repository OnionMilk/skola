#!/bin/python
import random

print("Hello World!")

antal_kast = range(10)

for i in antal_kast:
    dice_nr = random.randint(1, 6)
    print(dice_nr)
