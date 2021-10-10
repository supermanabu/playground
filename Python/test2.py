import sys, os
import numpy as np
home = os.path.expanduser("~")
sys.path.append(home + '/Playground/Python/ref')
import tl

a = [1,2,3,4]
print(np.mean(np.array(a)))