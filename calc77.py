'''
Created on May 5, 2021

@author: kivag
'''

def calc77(divisor, start, end):
    for n in range(start, end + 1):
        if n % divisor == 0 and n % 2 == 0:
            print(n, end=',')

    print()


def calc77_list(divisor, start, end):
    result = []
    for n in range(start, end + 1):
        if not (n % divisor) and not (n % 2):
            result.append(n)

    return result


def calc77_final(divisor, start, end):
    if start % 2:
        start += 1
    
    return [n for n in range(start, end + 1, 2) if not n % 111]
    

if __name__ == '__main__':
    calc77(111, 7000, 8658)
    calc77(111, 9000, 9546)
    
    print(calc77_list(111, 7000, 8658))
    print(calc77_list(111, 9000, 9546))

    print(calc77_final(111, 7000, 8658))
    print(calc77_final(111, 9000, 9546))