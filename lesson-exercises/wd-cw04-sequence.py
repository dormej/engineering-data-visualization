print("\nzad5")
import sys

class Ciagi:
    def __init__(self, a,n,r):
        self.a = a
        self.n = n
        self.r = r
    def wyswietl_dane(self):
        return (self.a,self.n,self.r)
    def wyswietl_wyrazy(self):
        for i in range (self.n):
           print(self.a+i*self.r)

    def suma(self):
        return(((2*self.a+(self.n-1)*self.r)/2) *self.n)

ciag1 = Ciagi(1,5,2)
print("wyraz1:",ciag1.a,"liczba wyrazow:",ciag1.n,"różnica:",ciag1.r)
print("suma:",ciag1.suma())
ciag1.wyswietl_wyrazy()


