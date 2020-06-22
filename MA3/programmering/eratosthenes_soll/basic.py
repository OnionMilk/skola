#!/bin/python

# Eratosthenes soll:
# Ideen är att loopa igenom listan med variabeln "i" och testa om "j" är delbart med "i"
# Är "j" delbart med "i" ska "i" tas bort ifrån listan.

numlist = []
resultat = []

limit = input("ange primtal limit: ")
limit = int(limit)

# Generering av listan:
for i in range(2, limit): # man måste börja med två
    numlist.append(i)


# Själva sollet:
for i in numlist:

    resultat.append(i)

    for j in numlist:
        if j == i:
            continue

        elif not(j % i):
            numlist.remove(j)


print("resultat: ", numlist)
