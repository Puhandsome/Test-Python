from math import gcd

class Fraction:
    def __init__(self, a, b):
        GCD = gcd(a,b)
        self.numerator = a//GCD
        self.denominator = b//GCD

    def __str__(self):
        a = self.numerator
        b = self.denominator
        if (a < 0 and b < 0 ) or (a>0 and b<0):
            a = -a
            b = -b
        return str(a)+"/"+str(b)

    def __eq__(self, p):
        return self.numerator * p.denominator == p.numerator * self.denominator

    def __add__(self, p):
        a = self.numerator * p.denominator + p.numerator * self.denominator
        b = self.denominator*p.denominator
        return Fraction(a,b)

    def __sub__(self, p):
        a = self.numerator * p.denominator - p.numerator * self.denominator
        b = self.denominator*p.denominator
        return Fraction(a,b)

    def __mul__(self, p):
        a = self.numerator * p.numerator
        b = self.denominator * p.denominator
        return Fraction(a,b)

    def __truediv__(self, p):
        a = self.numerator * p.denominator
        b = self.denominator * p.numerator
        return Fraction(a,b)

# Do not change the code below this line.
p = Fraction(int(input()), int(input()))
q = Fraction(int(input()), int(input()))
r = Fraction(int(input()), int(input()))
s = (p / q) * (p + q) - q
print(s)
print(s == r)
