# -*- coding: utf-8 -*-

from py_tools import *

"""
Created on Thu Jun  9 13:36:46 2016

@author: WELG
"""

data = []

file_name = input("Provide a name of a file of data ")

try:
    fh = open(file_name, 'r')  # testGradesData.py
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            # log(new[:-1])
            addIt = new[:-1].split(',')  #remove trailing \n
            data.append(addIt)
finally:
    # log(data)
    fh.close()  # close file even if fail


