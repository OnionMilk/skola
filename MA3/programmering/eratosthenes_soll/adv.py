#!/bin/python
# När man kör koden spottar den ut en del primtal men ochså en fyra ibland.
# Den lyckas aldrig räkna tvåan.


# Ideen är att loopa igenom listan med variabeln "i" och testa om "j" är delbart med "i"
# Är "j" delbart med "i" ska "i" tas bort ifrån listan.

class numobj(n):
    def __init__(self):
        self.numdict = {
            dyn: 0
            static: 0
            color: ""
        }

    def remove(self, n):
        self.numdikt.dyn = NaN


resultat = []

# Listan är väldigt kort så det blir lättare att titta på output.
# Jag har två listor, det finns säkert ett elegantare sätt, men det här får duga.
for i in range(1, 10):
    numlist_static.append(i)
    numlist_dynamic.append(i)


for i in numlist_dynamic:
    print("init: ", i)

    if i <= 1:
        print("i1: ", i)
        del(numlist_dynamic[i-1])
        print("numlist: ", numlist_dynamic, "\n")

    # Någonstans här går tvåan upp i rök.

    else:
        print("asdf: ", i)
        resultat.append(i)

        for j in numlist_static:
            print("i2start: ", i)
            print("jstart: ", j)

            if j == i:
                print("i2continue: ", i)
                print("jcontinue: ", j)
                print("%continue: ", j%i, "\n")
                continue

            elif not(j % i):
                numlist_dynamic.remove(j)
                print("i2remove: ", i)
                print("jremove: ", j)
                print("%remove: ", j%i, "\n")

            else:
                print("i2append: ", i)
                print("jappend: ", j)
                print("%append: ", j%i, "\n")


print("numlist_dynamic: ", numlist_dynamic)
print("numlist_static: ", numlist_static)
print("resultat: ", resultat)
