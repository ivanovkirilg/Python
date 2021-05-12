'''
Created on May 9, 2021

@author: kivag
'''

try:
    raise ValueError('argument')
except ValueError as ex:
    print('Exception arguments:', ex.args)
