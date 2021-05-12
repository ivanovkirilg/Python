'''
Created on May 9, 2021

@author: kivag
'''

class InvalidWithdrawal(Exception):
    
    def __init__(self, balance, amount):
        super().__init__(f"account doesn't have ${amount}")
        self.amount = amount
        self.balance = balance
        
    def overage(self):
        return self.amount - self.balance

try:
    raise InvalidWithdrawal(20, 50)
except InvalidWithdrawal as ex:
    print("Withdrawal larger than balance by", ex.overage(), 'leva')
