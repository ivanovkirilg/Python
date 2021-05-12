'''
Created on May 9, 2021

@author: kivag
'''

import random

some_exc = [ValueError, TypeError, IndexError, None]

try:
    chosen_exc = random.choice(some_exc)
    print(f'raising {chosen_exc}')
    if chosen_exc:
        raise chosen_exc

except ValueError:
    print('caught a ValueError')
except TypeError:
    print('caught a TypeError')
except Exception as my_exc:
    print('caught a %s' % my_exc.__class__.__name__)
else:
    print("didn't catch any exceptions")
finally:
    print('done with exceptions')


    
