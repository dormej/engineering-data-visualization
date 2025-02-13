# class Parzyste_Indeksy:
#    def __init__(self, numer):
#        self.numer = numer
#    def __iter__(self):
#        return self
#    def __next__(self):
#        for i in range (1,len(self.numer)):
#             if i % 2 == 0:
#                 print(self.numer[i])
#
# obiekt = Parzyste_Indeksy("01234567")
# print(next(obiekt))

class Samogloski:
    def __init__(self,tekst):
        self.i = 0
        self.tekst = tekst
        self.dlugosc = len(tekst)
        self.vowels = "aeiuoy"
    def __iter__(self):
        return self
    def __next__(self):
        i = self.i
        if self.i < self.dlugosc and self.tekst[i] in self.vowels:
            self.i += 1
            return self.tekst[i]
        elif self.i < self.dlugosc and self.tekst[i] not in self.vowels:
            self.i += 1
            return ""
        else:
            raise StopIteration()

slowo = Samogloski('aloa')
print("Czy wyraz:",(slowo.tekst),"ma samogloski ?\n", isinstance(slowo,Samogloski))
print(slowo)
print(next(slowo), end="")
print(next(slowo), end="")
print(next(slowo), end="")
print(next(slowo), end="")