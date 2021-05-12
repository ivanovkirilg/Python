'''
Created on May 5, 2021

@author: kivag
'''

class Square():

    def __init__(self, side_len):
        self.side = side_len   
    
    def perimeter(self):
        return self.side * 4
    
    def area(self):
        return self.side * self.side
    

if __name__ == '__main__':
    my_side = 2.56
    
    my_sq = Square(my_side)
    
    print(f'A square with side {my_sq.side}',
          f'has a perimeter of {my_sq.perimeter()}',
          f'and an area of {my_sq.area()}')