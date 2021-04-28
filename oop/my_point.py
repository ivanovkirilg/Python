'''
Created on Apr 25, 2021

@author: kivag
'''

import math

class Point:
    
    def __init__(self, x=0, y=0):
        self.move(x, y)
    
    def move(self, x, y):
        self.x, self.y = x, y
        
    def reset(self):
        self.move(0, 0)
    
    def dist(self, to):
        return math.sqrt( (self.x - to.x)**2 + (self.y - to.y)**2 )
    

a = Point()
b = Point()

a.reset()
b.move(5, 0)

print(b.dist(a))

assert b.dist(a) == a.dist(b)

a.move(3, 4)

print(a.dist(b))
print(a.dist(a))