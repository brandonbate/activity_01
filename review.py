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