# Answer the following questions by creating the specified functions and
# classes specified below.

import review

#1) Create a function hello_world that outputs the string "Hello World"
def test_hello():
    assert review.hello_world() == "Hello World"

#2) Create a function add that takes in two inputs and computes their sum.
def test_add():
    assert review.add(3,4) == 7
    assert review.add(-1.32, 58.38) == (-1.32 + 58.38)

#3) Create a function exponent that takes in two inputs a and b and computes a^b.
def test_exponent():
    assert review.exponent(3,4) == 81
    assert review.exponent(-2,3) == -8

#4) Create a function favorite_number that takes a number as input and gives an
# output string that states that "Your favorite number is ...".
def test_favorite_number():
    assert review.favorite_number(5) == "Your favorite number is 5"

#5) Create a function test_older that takes an numeric input and gives
# the type of string output displayed below.
def test_older():
    assert review.older(18) == "You are 18 years old. In 10 years you will be 28 years old."

#6) Create a dictionary called number_to_word_dict that converts the numbers
# 0, 1, 2, 3, ..., 10 to the strings "zero", "one", "two", "three", ... "ten".
def test_number_to_word_dict():
    assert list(review.number_to_word_dict.keys()) == list(range(11))
    assert review.number_to_word_dict[3] == 'three'
    assert review.number_to_word_dict[0] == 'zero'

#7) Create a function first_alphabetically that takes a list of strings as input,
# sort the list alphabetically, and return the first entry.
def test_first_alphabetically():
    assert review.first_alphabetically(['John', 'Paul', 'George', 'Ringo']) == 'George'
    assert review.first_alphabetically(['down', 'by', 'the', 'bay']) == 'bay'

#8) Create a function has_spam that takes in a string and tests if the string
# contains the word 'spam'.
def test_has_spam():
    assert review.has_spam("I think spam is the best tasting canned meat")
    assert not review.has_spam("Canned meat is a terrible idea.")
    assert review.has_spam("SPAM SPAM SPAM!!")

#9) Create a function square_numbers that takes an input n and returns a list of
# numbers 1^2, 2^2, 3^2, ..., n^2.
def test_square_numbers():
    assert review.square_numbers(4) == [1, 4, 9, 16]
    assert review.square_numbers(8) == [1, 4, 9, 16, 25, 36, 49, 64]

#10) Create a function next_square_number that takes an input n and returns the
# next square number.
def test_next_square_number():
    assert review.next_square_number(15.5) == 16
    assert review.next_square_number(83) == 100

from review import Fraction

#11) Create a class Fraction that has properties for the numerator and
# denominator. Define a member function that gives a string representation
# of the Fraction.
def test_fraction_str():
    f = Fraction(3,5)
    assert str(f) == '3/5'

#12) Create a multiply method for the Fraction class.
def test_fraction_multiply_with_str():
    f1 = Fraction(2,-7)
    f2 = Fraction(3,5)
    assert str(f1.multiply(f2)) == '6/-35'

#13) Create a method that tests for equality for the Fraction class.
def test_fraction_multiply():
    f1 = Fraction(2,5)
    f2 = Fraction(3,4)
    assert f1.multiply(f2) == Fraction(3,10)

#14) Create a divide method for the Fraction class.
def test_fraction_divide():
    f1 = Fraction(-3,7)
    f2 = Fraction(12,13)
    assert f1.divide(f2) == Fraction(-3*13,12*7)

#15) Create an add method for the Fraction class.
def test_fraction_add():
    f1 = Fraction(5,8)
    f2 = Fraction(-3,7)
    assert f1.add(f2) == Fraction(5*7 - 3*8, 7*8)

from review import Rectangle

#16) Create a Rectangle class that stores the width and length of the
# rectangle. Create a method that provides the string representation below.
def test_rectangle_str():
    r = Rectangle(3.4, 1.7)
    assert str(r) == "Rectangle with width=3.4 and length=1.7"

#17) Create an area method for the Rectangle class.
def test_rectangle_area():
    r = Rectangle(2.7, 6.5)
    assert r.area() == 2.7*6.5

from review import Square

#18) Create a subclass Square of Rectangle.
def test_square_is_subclass():
    assert issubclass(Square, Rectangle)

#19) Nothing to do here if #18 is successful. The area method should be
# inherited automatically.
def test_square_area():
    s = Square(6.5)
    assert s.area() == 6.5*6.5

#20) Create a method for creating string representation for Square.
def test_square_str():
    s = Square(8.34)
    assert str(s) == "Square with length=8.34"