""" 
Use this to generate a file always updating
to easily test the program
python generate.py -u  > log for example
"""

import random
import time

while True:
    print(random.random())
    time.sleep(0.8)

