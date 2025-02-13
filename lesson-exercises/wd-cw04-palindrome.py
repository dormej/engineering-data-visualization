
print("zad6")

class Slowa:
    def __init__(self, wyraz1,wyraz2):
        self.wyraz1 = wyraz1
        self.wyraz2 = wyraz2
    def spr_czy_palindrom(self):
        r = self.wyraz1[::-1]
        if (self.wyraz1 == r):
            return "Wyraz jest palindromem."
        else:
            return "Wyraz nie jest palindromem."
    def spr_czy_metagramy(self):
        ile=0
        for i in range (len(self.wyraz1)):
            if (self.wyraz1[i] != self.wyraz2[i]):
                ile +=1
        if (ile == 1):
            return "Metagramy"
        else:
            return "Nie metagramy"
    def spr_czy_anagramy(self):
        if (sorted(self.wyraz1)==sorted(self.wyraz2)):
            return "Anagramy"
        else:
            return "Nie anagramy"
    def wyswietl(self):
        return self.wyraz1, self.wyraz2

slowo1 = Slowa("kajak","jakka")

print(slowo1.spr_czy_palindrom())
print(slowo1.spr_czy_metagramy())
print(slowo1.spr_czy_anagramy())
print(slowo1.wyswietl())