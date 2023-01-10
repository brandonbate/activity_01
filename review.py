
def hello_world():
	return "Hello World"

def add(a, b):
    return a+b
    
def exponent(a, b):
    return a**b
    
def favorite_number(a):
    return "Your favorite number is " + str(a)
    
def older(a):
    return "You are " + str(a) + " years old. In 10 years you will be " \
            + str(a+10) + " years old."

number_to_word_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', \
                       6:'size', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}

def first_alphabetically(a):
    b = sorted(a)
    return b[0]
    
def has_spam(a):
    return 'spam' in a.lower().split()

def square_numbers(n):
    return [i**2 for i in range(1,n+1)]

import math

def next_square_number(n):
    return int(math.ceil(math.sqrt(n)))**2

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
        
    def multiply(self, f):
        return Fraction(self.num * f.num, self.den * f.den)
    
    def divide(self, f):
        return Fraction(self.num * f.den, self.den * f.num)

    def add(self, f):
        return Fraction(self.num * f.den + f.num * self.den, self.den * f.den)
        
    def __eq__(self, other):
        return (self.num * other.den == other.num * self.den)

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width
        
    def __str__(self):
        return "Rectangle with width=" + str(self.width) + " and length=" + \
                str(self.length)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return "Square with length=" + str(self.length)