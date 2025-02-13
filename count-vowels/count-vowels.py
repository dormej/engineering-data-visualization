def ile_samoglosek(napis):
    ile = 0
    vowels = "aeiou"
    for litera in napis:
        if litera in vowels:
            ile += 1
    return ile


litery = ['a', 'b', 'c', 'd', 'e', 'f']
ile = 0
ile2 = 0
f = open("napisy.txt", "w+")
# pętla 8 razy
for i in range(0, 6):
    for j in range(0, 6):
        for k in range(0, 6):
            for l in range(0, 6):
                for m in range(0, 6):
                    for n in range(0, 6):
                        for o in range(0, 6):
                            for u in range(0, 6):
                                napis = litery[i] + litery[j] + litery[k] + litery[l] + litery[m] + litery[n] + litery[
                                    o] + litery[u]
                                f.write(napis + '\n')
                                if (ile_samoglosek(napis) < 4):
                                    ile += 1

f.close()
print(ile)