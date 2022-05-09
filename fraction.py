from math import gcd, lcm


class MathMixin():
    @staticmethod
    def add(fract1, fract2):
        # наименьшее общее кратное
        den = lcm(fract1.den, fract2.den)
        num = den // fract1.den * fract1.num + den // fract2.den * fract2.num
        return cls(num, den)

    @staticmethod
    def sub(fract1, fract2):
        # наименьшее общее кратное
        den = lcm(fract1.den, fract2.den)
        num = den // fract1.den * fract1.num - den // fract2.den * fract2.num
        return cls(num, den)

    @staticmethod
    def mull(fract1, fract2):
        num = fract1.num * fract2.num
        den = fract1.den * fract2.den
        # наибольший общий делитель
        g_c_d = gcd(num, den)
        # сокращаем дробь, если это необходимо
        if g_c_d > 1:
            num //= g_c_d
            den //= g_c_d
        return cls(num, den)

    @staticmethod
    def div(fract1, fract2):
        num = fract1.num * fract2.den
        den = fract1.den * fract2.num
        # наибольший общий делитель
        g_c_d = gcd(num, den)
        # сокращаем дробь, если это необходимо
        if g_c_d > 1:
            num //= g_c_d
            den //= g_c_d
        return cls(num, den)


class Fraction(MathMixin):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        # наибольший общий делитель
        g_c_d = gcd(self.__num, self.__den)
        # сокращаем дробь, если это необходимо
        if g_c_d > 1:
            self.__num //= g_c_d
            self.__den //= g_c_d

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        # !!! assert is used when debugging code
        # ??? assert заменить на if-else
        assert isinstance(num, int), f"{num} - Нужно передать целое число"
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        # assert is used when debugging code!!!
        assert isinstance(den, int), f"{num} - Нужно передать целое число"
        self.__den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __sub__(self, fract):
        den = lcm(self.den, fract.den)
        num = den // self.den * self.num - den // fract.den * fract.num
        return self.__class__(num, den)

    def __add__(self, fract):
        # наименьшее общее кратное
        den = lcm(self.den, fract.den)
        num = den // self.den * self.num + den // fract.den * fract.num
        return self.__class__(num, den)

    def __mul__(self, fract):
        num = self.num * fract.num
        den = self.den * fract.den
        return self.__class__(num, den)

    def __truediv__(self, fract):
        num = self.num * fract.den
        den = self.den * fract.num
        return self.__class__(num, den)

    @classmethod
    def from_string(cls, string):
        # ???????????
        # нужен ли здесь try/except, чтобы отлавливать ошибки, которые
        # возникают при провале преобразования строки в целое
        num = int(string.split("/")[0])
        den = int(string.split("/")[1])
        return cls(num, den)


if __name__ == "__main__":
    from fractions import Fraction as F
    from random import randint

    def fract_gen(a, b):
        yield (Fraction(randint(a, b), randint(a, b)),
               Fraction(randint(a, b), randint(a, b)))

    for i in range(5):
        for f1, f2 in fract_gen(1, 10):
            print(f"F1: {f1}, F2: {f2}")
            print(f"{f1} + {f2} = {f1 + f2}")
            print(f"{f1} - {f2} = {f1 - f2}")
            print(f"{f1} * {f2} = {f1 * f2}")
            print(f"{f1} / {f2} = {f1 / f2}")
            print("-" * 20)

#     F1 = F(7, 8)
#     F2 = F(9, 10)
#
#     f1 = Fraction(7, 8)
#     f2 = Fraction(9, 10)
#
#     print(Fraction.add(f1, f2))
#     print(F1 + F2)
#
#     print(Fraction.sub(f1, f2))
#     print(F1 - F2)
#
#     print(Fraction.mull(f1, f2))
#     print(F1 * F2)
#
#     print(Fraction.div(f1, f2))
#     print(F1 / F2)
#
#     print()
#     print(Fraction.from_string("10/100"))
