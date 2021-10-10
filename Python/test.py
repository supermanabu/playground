import sys, os
import numpy as np
home = os.path.expanduser("~")
sys.path.append(home + '/Playground/Python/ref')
import tl
import numpy as np
import matplotlib
matplotlib.rcParams['backend'] = 'SVG'
import matplotlib.pyplot as plt

plt.plot([1,2,3])
plt.savefig('kankan_2.svg', format='svg')