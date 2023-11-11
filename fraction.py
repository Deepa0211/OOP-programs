class Fraction():
    numerator = None
    denominator = None
    
    def __init__(self, x, y):
        self.numerator = int(x)
        self.denominator = int(y)
    
    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)
    
    def __add__(self, other):
        tempN = self.numerator * other.denominator + self.denominator * other.numerator
        tempD = self.denominator * other.denominator
        
        return Fraction(tempN, tempD)
    
    def __sub__(self, other):
        tempN = self.numerator * other.denominator - self.denominator * other.numerator
        tempD = self.denominator * other.denominator
        
        return Fraction(tempN, tempD)
    
    def __mul__(self, other):
        tempN = self.numerator * other.numerator
        tempD = self.denominator * other.denominator
        
        return Fraction(tempN, tempD)
    
    def __truediv__(self, other):
        tempN = self.numerator * other.denominator
        tempD = self.denominator * other.numerator
        
        return Fraction(tempN, tempD)