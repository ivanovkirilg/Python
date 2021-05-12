'''
Created on Apr 28, 2021

@author: kivag
'''

class Human():
    
    def __init__(self, name, crippled_arms=0, crippled_legs=0):
        self.name = name
        self.arms = 2 - crippled_arms
        self.legs = 2 - crippled_legs


class Spider():
    
    def __init__(self, crippled_legs=0):
        self.legs = 8 - crippled_legs


class Student(Human):
    
    def __init__(self, name, mark):
        Human.__init__(self, name)
        self.mark = mark



# ivan = Human()
# petko = Human(1)
#
# sophroniy = Spider(2)
#
# print(f'Ivan has {ivan.arms} arms and {ivan.legs} legs')
# print(f'Petko has {petko.arms} arms and {petko.legs} legs')
#
# print(f'Sophko has {sophroniy.legs} legs')


ivancho = Student('Ivan Terziyski', 95)
print("{} has {}/100".format(getattr(ivancho, 'name'), getattr(ivancho, 'mark')))

setattr(ivancho, 'mark', 80)
print("{} has {}/100".format(getattr(ivancho, 'name'), getattr(ivancho, 'mark')))







