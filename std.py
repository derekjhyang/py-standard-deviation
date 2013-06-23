#!/usr/bin/env python

# here we implements a std function and then compares it
# with numpy.std() function

import math
import numpy

def std(list):
    avg = sum(list)/float(len(list))
    return math.sqrt(sum(map(lambda x: (x-avg)**2, list))/len(list))




if __name__ == "__main__":
   a = range(1,100000)
   print std(a)
   print numpy.std(a)
