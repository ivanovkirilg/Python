'''
Created on May 9, 2021

@author: kivag
'''

def any_division(number):
    try:
        if number == 13:
            raise ValueError('unlucky!')
        return 100/number
    except ZeroDivisionError:
        return 'division by zero?!'
    except TypeError:
        return 'numbers only, please'
    except ValueError:
        print('you are unlucky')
        raise


def div_with_ex(number, divisor):
    try:
        print(number, '/', divisor, '=', number / divisor * 1.0)
    except ZeroDivisionError:
        print("You can't divide by zero")

def div_with_if(number, divisor):
    if divisor == 0:
        print("You can't divide by zero")
    else:
        print(number, '/', divisor, '=', number / divisor * 1.0)


div_with_ex(5, 3)
div_with_ex(5, 0)

div_with_if(5, 3)
div_with_if(5, 0)


