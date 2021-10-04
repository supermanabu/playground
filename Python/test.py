import os, sys
home = os.path.expanduser("~")
sys.path.append(home + '/Playground/Python/ref')
import tl
from read_POSCAR import POSCAR

import numpy as np

a = 33347
while a <= 33367:
	print(a)
	a += 1