import os
import random

v1 = 0

for i in range(16):
    if v1 != 0:
        print("Forkeando")
        v1 = os.fork()
    else:
        print(f'i = {i}; fork = {v1}; pid = {os.getpid()}')