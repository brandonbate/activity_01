import review

def test_hello():
    assert review.hello_world() == "Hello World"
    
def test_add():
    assert review.add(3,4) == 7
    assert review.add(-1.32, 58.38) == (-1.32 + 58.38)
    
def test_exponent():
    assert review.exponent(3,4) == 81
    assert review.exponent(-2,3) == -8
    
def test_favorite_number():
    assert review.favorite_number(5) == "Your favorite number is 5"
    
def test_older():
    assert review.older(18) == "You are 18 years old. In 10 years you will be 28 years old."
    
def test_number_to_word_dict():
    assert list(review.number_to_word_dict.keys()) == list(range(11))
    assert review.number_to_word_dict[3] == 'three'
    assert review.number_to_word_dict[0] == 'zero'
    
def test_first_alphabetically():
    assert review.first_alphabetically(['John', 'Paul', 'George', 'Ringo']) == 'George'