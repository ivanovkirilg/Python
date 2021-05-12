'''
Created on May 12, 2021

@author: kivag
'''

import os

print('renaming file...')
os.rename('CA.txt', 'CodeAcademy.txt')

input('file renamed')

print('renaming it back...')
os.rename('CodeAcademy.txt', 'CA.txt')
