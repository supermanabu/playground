import os, sys
home = os.path.expanduser("~")
sys.path.append(home + '/Playground/Python/ref')
import tl
from read_POSCAR import POSCAR

import numpy as np

a = 5
b = 1102
c = (a>b and [a] or [b])[0]
print(c)