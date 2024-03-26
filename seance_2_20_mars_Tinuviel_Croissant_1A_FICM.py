from math import gcd

# self est le constructeur

## exercice 1 : représentation de fraction
# documenter classe et constructeur de Fraction

class Fraction :
    def __init__(self,n,d):
        ''' prend deux entiers relatifs n et d, renvoie la fraction de numérateur n et de dénominateur d sous la forme d'un uplet (n,d) '''
        self.num = n
        self.den = d

    def __str__(self):
        return f"my value is : {(self.num,self.den)}"


## exercice 2 : donner des opérations à la classe
# gcd trouve le plus grand commun diviseur

class Fraction :
    def __init__(self,n,d):
        self.num = n
        self.den = d

    def symplify(self):
        d = gcd(self.num,self.den)
        return Fraction(self.num // d, self.den //d)

    def mult(self,other):
        return Fraction((self.num) * (other.num),(self.den) * (other.den))

    def add(self,other):
        return Fraction((self.num) * (other.den) + (other.num) * (self.den), (self.den) * (other.den))

    def __str__(self):
        return f"my value is : {(self.num,self.den)}"

F=Fraction(3,4)
print(F.__str__())
print((F.add(Fraction(1,2))).__str__())


## exercice 3

def H(n):
    F=Fraction(1,1)
    for i in range(2,n+1):
        F = F.add(Fraction(1,i))
    return f"my value is :{F}"

## exercice 4

def Leibniz(n):
    F=Fraction(1,1)
    k=1
    for i in range(3,2*n+1,2):
        F = F.add(Fraction(k,i))
        k = -k
    return f"my value is :{F}"

























