'''
Created on May 5, 2021

@author: kivag
'''

from math import pi

class Cylinder():

    def __init__(self, r, h):
        self.radius = r
        self.height = h
        
    def base_area(self):
        return pi * self.radius * self.radius
    
    def side_area(self):
        return 2 * pi * self.radius * self.height
    
    def area(self):
        return 2 * self.base_area() + self.side_area()
    
    def volume(self):
        return self.base_area() * self.height
    

if __name__ == '__main__':
    my_cyl = Cylinder(5, 10)
    
    print(my_cyl.area(), my_cyl.volume())
    print(my_cyl.base_area(), my_cyl.side_area())