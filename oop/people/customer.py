'''
Created on May 5, 2021

@author: kivag
'''

class Customer():
    curr_id = 0
    
    def __init__(self, cart):
        self.cart = cart
        
        self.id = Customer.curr_id
        Customer.curr_id += 1
    
    
    def display_cart(self):
        print('Cart:', self.cart)


class ReturningCustomer(Customer):
    
    def __init__(self, customer, new_cart):
        self.id = customer.id
        self.history = []
        self.history.append(customer.cart)
        self.cart = new_cart
        
