'''
Created on May 12, 2021

@author: kivag
'''

test = open('CA.txt', 'w+')

print('Filename:', test.name)
print('Closed:', test.closed)
print('Open Mode:', test.mode)

test.write('hello\nworld!\n')

test.seek(0, 0)

test.write('abcde')

print('\n' + 'Closing...' + '\n')
test.close()
print('Closed:', test.closed)
