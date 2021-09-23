import sys, os
import numpy as np
home = os.path.expanduser("~")
sys.path.append(home + '/Playground/Python/ref')
import tl

# WARNING: 'Direct' must exist in the file

class POSCAR():
	def __init__(self, filename):
		self.filename = filename

	def contents(self):
		return tl.line(self.filename)

	def title(self):
		return self.contents()[0]

	def scaling_factor(self):
		return float(self.contents()[1].strip())

	def a(self):
		a_str = self.contents()[2]
		a = np.array(tl.lls(a_str, 'float')) * self.scaling_factor()
		return a.tolist()

	def b(self):
		b_str = self.contents()[3]
		b = np.array(tl.lls(b_str, 'float')) * self.scaling_factor()
		return b.tolist()

	def c(self):
		c_str = self.contents()[4]
		c = np.array(tl.lls(c_str, 'float')) * self.scaling_factor()
		return c.tolist()

	def norm_a(self):
		return np.linalg.norm(self.a())

	def norm_b(self):
		return np.linalg.norm(self.b())

	def norm_c(self):
		return np.linalg.norm(self.c())

	def alpha(self):
		return tl.angle(self.b(), self.c())

	def alpha_degree(self):
		return tl.angle(self.b(), self.c(), 2)

	def beta(self):
		return tl.angle(self.c(), self.a())

	def beta_degree(self):
		return tl.angle(self.c(), self.a(), 2)

	def gamma(self):
		return tl.angle(self.a(), self.b())

	def gamma_degree(self):
		return tl.angle(self.a(), self.b(), 2)

	def volume(self):
		return tl.vol_prllp(self.a(), self.b(), self.c())

	def area_ab(self):
		return np.linalg.norm(np.cross(self.a(), self.b()))

	def area_bc(self):
		return np.linalg.norm(np.cross(self.b(), self.c()))

	def area_ca(self):
		return np.linalg.norm(np.cross(self.c(), self.a()))

	def elements(self):
		elements = self.contents()[5].split()
		return elements

	def element_rank(self, element, occurrence=1):
		return tl.index_v2(self.elements(), element, occurrence) + 1

	def element_numbers(self):
		return tl.lls(self.contents()[6], 'int')

	def natom(self):
		return sum(self.element_numbers())

	def element_number(self, element, occurrence=1):
		return self.element_numbers()[self.element_rank(element, occurrence)-1]

	def natom_before(self, element, occurrence=1):
		return sum(self.element_numbers()[:self.element_rank(element, occurrence)-1])
		
	def atom_startline(self):
		i = 0
		while True:
			if 'Direct' in self.contents()[i]:
				startline = i + 1
				break
			i += 1
		return startline + 1

	def atom_endline(self):
		return self.atom_startline() + self.natom() - 1

	def atoms(self):
		atoms_str = self.contents()[self.atom_startline()-1:self.atom_endline()]
		return [tl.lls(atom, 'float') for atom in atoms_str]

	def atoms_e(self, element, occurrence=1):
		return self.atoms()[self.natom_before(element, occurrence):self.natom_before(element, occurrence)+self.element_number(element, occurrence)]
		
	def atom(self, index):
		return self.atoms()[index-1]

	# index counted inside the specified element
	def atom_e(self, element, index, occurrence=1):
		return self.atoms()[index+self.natom_before(element, occurrence)-1]
