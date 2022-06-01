#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#
def filledOrders(order, k):
    box = []
    c = 0
    order.sort()
    if order[0] > k:
        ans = 0
    else:
        c=order[0]
        box.append(c)
        for i in range(1,len(order)):
            if c+order[i] <= k:
                box.append(c)
                c+=order[i]
                
                
            elif c+order[i] > k:
                break
        ans = len(box)
    return ans

