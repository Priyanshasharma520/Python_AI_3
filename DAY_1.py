import os

for i in dir(os):
    if 'dir' in i:
        print(i)
