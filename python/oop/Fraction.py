
class Fraction(object):

    def __init__(self, num=0, den=1):
        common = self.gcd(num, den)
        self.num = num // common
        self.den = den // common

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return "{}{}{}".format(self.num, "/", self.den)

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        return self * Fraction(other.den, other.num)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __le__(self, other):
        return self.num * other.den <= self.den * other.num

    def __ge__(self, other):
        return self.num * other.den >= self.den * other.num
