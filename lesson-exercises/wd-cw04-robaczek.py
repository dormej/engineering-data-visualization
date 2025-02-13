print("zad7")
import sys

class Rob:
    def __init__(self, x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self):
        ile_w_g = int(input("Gora: "))
        odl_w_g = self.krok*ile_w_g
        self.y = self.y + odl_w_g
        print("Wsp. x =", self.x, " y = ",self.y )
    def idz_w_dol(self):
        ile_w_d = int(input("Dol: "))
        odl_w_d = self.krok *(-1)*ile_w_d
        self.y = self.y + odl_w_d
        print("Wsp. x= ",self.x, " y =", self.y)
    def idz_w_prawo(self):
        ile_w_p = int(input("Prawo: "))
        odl_w_p = self.krok *ile_w_p
        self.x = self.x + odl_w_p
        print("Wsp. x =", self.x," y =", self.y)
    def idz_w_lewo(self):
        ile_w_l = int(input("Lewo: "))
        odl_w_l = self.krok *(-1)*ile_w_l
        self.x = self.x + odl_w_l
        print("Wsp. x =", self.x, " y =", self.y)


rob = Rob(0,0,2)
print("Wsp. x=",rob.x, "y=",rob.y, " krok to ",rob.krok," jedn.")
print("q = koniec, g = gora, d = dol, p = prawo, l =lewo")
w = ''
while( w!='q' ):
        w = input("Wybierz: q,g,d,p,l: ")
        if ( w == 'q' ):
            print("Koniec")
        if ( w == 'g'):
            rob.idz_w_gore()
        if ( w == 'd'):
            rob.idz_w_dol()
        if ( w == 'p'):
            rob.idz_w_prawo()
        if ( w == 'l'):
            rob.idz_w_lewo()
