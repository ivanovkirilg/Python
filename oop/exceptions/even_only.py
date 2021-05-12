'''
Created on May 9, 2021

@author: kivag
'''

class EvenOnly(list):
    
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError('Only integers can be added.')

        if integer % 2:
            raise ValueError('Only adding even numbers is recommended')
        
        super().append(integer)

instance = EvenOnly()
instance.append(4)
instance.append(-4)
# instance.append(4.0)
# instance.append('4')
# instance.append(3)
# instance.append(-3)
print(instance)











