'''
Created on May 5, 2021

@author: kivag
'''

class Employee():

    def __init__(self, name):
        self.employee_name = name

    def daily_rate(self, hours):
        return hours * 20
    

class PartTimeEmployee(Employee):
    
    def daily_rate(self, hours):
        return hours * 25
    

if __name__ == '__main__':
    print(Employee('Jack').daily_rate(8))
    
    print(PartTimeEmployee('John').daily_rate(4))
    