print(1,2,3,4)
print(1,2,3,4, sep='')

a=16
b=2.35
c=90
print('{:5d} {:6.3f} {:10d}'.format(a,b,c))
"""d=deciamal, f=float, 5 spacj, 6 znakow zarezerwowanych na te zmienna"""
print('{2:5d} {1:6.3f} {0:10d}'.format(a,b,c))
