'''
Created on May 5, 2021

@author: kivag
'''

class Stuff():
    name = 'Stuff'
    weight = 1.0
    value = 0.0
    condition = 1.0
    function = None


    def __init__(self, name, weight, value=0.0, condition=1.0, function=None):
        self.name = name
        self.weight = weight
        self.value = value
        self.condition = condition
        self.function = function
        
    def get_info(self):
        return {
            'name': self.name,
            'weight': self.weight, 
            'value': self.weight, 
            'condition': self.condition }
    
    def revalue(self, new_value):
        '''Returns the change in value that has been made.'''
        change = new_value - self.value
        self.value = new_value
        return change
    
    def repair(self, amount=1.0):
        self.condition += amount
        self.condition = min(self.condition, 1.0)
    
    def use(self, *args, **kwargs):
        '''Perform the object's function (if any) and deteriorate its condition.'''
        if self.function:
            self.function(args, kwargs)
        
        self.condition -= 0.1
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        