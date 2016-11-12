class Fraction:
   
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.value = self.numerator / self.denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)


    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.value == other.value

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        common = self.simplify_fraction(new_numerator, new_denominator)
        if int(new_numerator/common) == int(new_denominator/common):
            return 1
        return "{} / {}".format(int(new_numerator/common), int(new_denominator/common))
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        common = self.simplify_fraction(new_numerator, new_denominator)
        if int(new_numerator/common) == int(new_denominator/common):
            return 1
        return "{} / {}".format(int(new_numerator/common), int(new_denominator/common))
    
    def __sub__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator       
        if int(new_numerator) == 0:
            return 0
        return "{} / {}".format(int(new_numerator), int(new_denominator))

        
    def simplify_fraction(self, den, num):
        while num % den != 0:
            old_den = den
            old_num = num

            den = old_num
            num = old_den % old_num
        return den

    
a = Fraction(1, 2)
b = Fraction(2, 4)

print(a+b)
print(a == b)
print(a * b)
print(a - b)
