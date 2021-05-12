'''
Created on Apr 23, 2021

@author: kivag
'''

highest_float = 1.79e308
infinity_float = 1.8e308

unlimited_powa = 2791273712765386719283918273916426413621738172637182731327

my_dict = {
    'fruit': 'apple',
    'vegetable': 'cucumber',
    'weights': {
        'fruit': 1.5,
        'vegetable': 2.5
    }
}

my_list = [0, 1, 'two', {'three': 3}, 4, 'five']

my_tup = (5, 10, 15)

my_set = {2, 4, 8}


if __name__ == '__main__':

    input('\n--- Numbers --- ')  # # #

    print('1.79e308 is correctly stored as', highest_float)
    print('1.8e308 is incorrectly stored as', infinity_float)
    print('type():', type(highest_float))
    print('unlimited integers:', unlimited_powa)
    

    input('\n--- Dictionaries --- ')  # # #

    print(my_dict['fruit'], ':', my_dict['weights']['fruit'], 'kg')
    print(len(my_dict), 'items in dict')


    input('\n--- Strings --- ')  # # #

    print(r"raw\backslash double\\backslash")
    print("non-raw\backslash double\\backslash")
    print("unicode chars: \u2192 \N{rightwards arrow}")


    input('\n--- Booleans --- ')  # # #

    print('empty string:', bool(""))
    print('negative number:', bool(-5))


    input('\n--- Lists --- ')  # # #

    print('initial list:', my_list)
    my_list.append(6)
    print('append 6:', my_list)
    print('first non-zero element:', my_list.index(True))
    my_list.remove(0)
    print('remove 0:', my_list)
    print('elements 2-5:', my_list[2:5])
    print('last 3 elements:', my_list[-3:])
    print('in reverse order:', my_list[-1:-4:-1])


    input('\n--- Tuples --- ')  # # #

    print('tuple:', my_tup)
    first, second, third = my_tup
    print('sum:', first + second + third)
    # my_tup[1] = -5 # invalid


    input('\n--- Sets --- ')  # # #

    print('set:', my_set)
    print('4 in set:', my_set & {4} != set(), '(using intersection)')
    print('4 in set:', 4 in my_set, '(using "in" keyword)')
    print('union 6:', my_set | {6})

