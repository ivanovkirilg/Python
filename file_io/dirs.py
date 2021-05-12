'''
Created on May 12, 2021

@author: kivag
'''

import os

os.mkdir('test')
os.chdir('test')
print(os.getcwd())

os.chdir('..')
os.rmdir('test')
print(os.getcwd())
