'''
Created on May 9, 2021

@author: kivag
'''

def no_return():
    print('About to raise exception')
    raise Exception('Stop execution')
    print('Never executed')
    return 'not returned'

def call_exceptor():
    print('call_exceptor starting')
    no_return()
    print('not executed after exception')
    
    
try:
    no_return()
except:
    print('exception caught')

print('after exception')