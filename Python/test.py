import os, sys
home = os.path.expanduser("~")
sys.path.append(home + '/Playground/Python/ref')
import tl
from read_POSCAR import POSCAR

a = POSCAR('CONTCAR')
for i in a.atoms_e('N'):
	print(i)