'''
Created on May 12, 2021

@author: kivag
'''

test = open('alphabet.txt', 'r')

data = test.read(5)
print('first 5 letters:', data)

test.seek(0, 2)
position = test.tell()
test.seek(position - 5, 0)

data = test.read()
print('last 5 letters:', data)

test.seek(-10, 1)
data = test.read()
print('last 10 letters:', data)

test.close()
