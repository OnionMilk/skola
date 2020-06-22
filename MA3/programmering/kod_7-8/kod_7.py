#!/bin/python
import random

print("Hello World!")

spara_kasten = []

antal_kast = 5

for i in range(antal_kast):
    dice_nr = random.randint(1,6)
    spara_kasten.append(dice_nr)

print(spara_kasten)

antal_ettor = spara_kasten.count(1)

print(antal_ettor)
