'''
Created on Apr 28, 2021

@author: kivag
'''


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __gt__(self, other):
        if self.x + self.y > other.x + other.y:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.x + self.y < other.x + other.y:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def log(self):
        print(f"({self.x}, {self.y})")


class Greeting:
    def __init__(self, msg):
        self.message = msg

    def greet(self, name=None):
        if name is not None:
            print(f"{self.message}, {name}!")
        
        else:
            print(f"{self.message}!")


def sum(*args):
    if type(args[0]) == str:
        result = ''
    elif type(args[0]) == int or type(args[0]) == float:
        result = 0
        
    for x in args:
        result += x

    return result

if __name__ == '__main__':
    
    # input('\n--- Built-in --- ')  # # #
    # print(1 + 2)
    # print('Hello ' + 'world!')
    #
    # print(3 * 4)
    # print('hi! ' * 3)
    #
    # fruits = ['apples', 'oranges']
    # print(fruits * 2)
    #
    #
    # input('\n--- User-defined --- ')  # # #
    # a = Point(2, 3)
    # b = Point(1, -1)
    #
    # c = a + b
    # c.log()
    #
    # print(a > b, c > a)
    # print(a < b, b < c)
    # a.log()
    # print(a == Point(2, 3), c == b)
    #
    #
    # input('\n--- Function (None) --- ')  # # #
    # hi = Greeting('Hi')
    # hello = Greeting('Hello')
    #
    # hi.greet('Jack')
    # hi.greet()
    #
    # hello.greet('Jack')
    # hello.greet()
    #
    #
    # input('\n--- Function (type arg) --- ')  # # #
    # print(sum(3, 5, 7))
    # print(sum(1.2, 3.5, 2.3))
    # print(sum('a', 'b', 'c'))
    
    
    