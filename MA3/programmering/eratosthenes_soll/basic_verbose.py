#!/bin/python
# När man kör koden spottar den ut en del primtal men ochså en fyra ibland.
# Den lyckas aldrig räkna tvåan.


# Ideen är att loopa igenom listan med variabeln "i" och testa om "j" är delbart med "i"
# Är "j" delbart med "i" ska "i" tas bort ifrån listan.

numlist = []
resultat = []

# Listan är väldigt kort så det blir lättare att titta på output.
# Jag har två listor, det finns säkert ett elegantare sätt, men det här får duga.
for i in range(2, 100):
    numlist.append(i)

print("numlist: ", numlist, "\n")

for i in numlist:
    print("init: ", i)

    if i == 1:
        print("i1: ", i)
        numlist.remove(i)
        print("numlist: ", numlist, "\n")
        continue

    # Någonstans här går tvåan upp i rök.

    elif i >= 1:
        print("asdf: ", i)
        resultat.append(i)
        print("numlist???: ", numlist, "\n")

        for j in numlist:
            print("i2start: ", i)
            print("jstart: ", j)
            print("numlist: ", numlist,)

            if j == i:
                print("i2continue: ", i)
                print("jcontinue: ", j)
                print("%continue: ", j%i, "\n")
                continue

            elif not(j % i):
                numlist.remove(j)
                print("i2remove: ", i)
                print("jremove: ", j)
                print("%remove: ", j%i, "\n")

            else:
                print("i2append: ", i)
                print("jappend: ", j)
                print("%append: ", j%i, "\n")


print("resultat: ", numlist)
