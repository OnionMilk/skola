#!/bin/python
import numpy as np
import random

print("Hello World!")

spara_kasten = []

antal_kast = 50

for i in range(antal_kast):
    dice_nr = random.randint(1, 6)
    spara_kasten.append(dice_nr)

print("spara_kasten: ", spara_kasten)

antal_ettor = spara_kasten.count(1)

print("antal_ettor: ", antal_ettor)

sannolikheten_för_etta = antal_ettor / antal_kast

print("sannolikheten_för_etta: ", sannolikheten_för_etta)
