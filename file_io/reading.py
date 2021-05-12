'''
Created on May 12, 2021

@author: kivag
'''

test = open('CA.txt', 'r')
# test = open('CA.txt', 'r+') # can write
# test = open('CA.txt', 'w+') # overwrites file (can read)

contents = test.read()
print('file contents:', contents, sep='\n')

test.close()
