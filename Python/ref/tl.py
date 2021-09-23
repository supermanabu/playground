import sys, os, math, sympy
import numpy as np
from random import uniform
import matplotlib.pyplot as plt

#1 the Origin is the point (0, 0, 0)
#1 About vectors
#2 By default a (formatted) vector is a list which indicates its end, with its origin at the Origin. 
#1 About matrices
#2 A matrix is a list of lists. Each list in the matrix is a row. 
#1 About planes
#2 By default a plane is a list which contains its normal (by default the normal's origin is at the Origin) and an in-plane point. 
#! A coord system is a list containing three lists; the three lists are a, b, c

#!--------------------Vectors and scalars--------------------!#
#!----------About Angles----------!#
# Get angle between two vectors
def angle(v1, v2, kind=1):     # kind == 1: in radians; kind == 2: in degrees
	norm_1 = np.linalg.norm(v1)
	norm_2 = np.linalg.norm(v2)
	angle_f = math.acos(np.inner(v1, v2) / (norm_1 * norm_2))
	if kind == 2:
		angle_f = angle_f * 180 / math.pi
	return angle_f
# Receive a vector and a plane / Return the angle between them in RADIANS
def angle_vp(v, p, kind=1):
	angle_temp = angle(v, p[0])
	if angle_temp <= math.pi/2:
		angle_f = math.pi/2 - angle_temp
	elif angle_temp > math.pi/2:
		angle_f = angle_temp - math.pi/2
	if kind == 2:
		angle_f = angle_f * 180 / math.pi
	return angle_f
#?----------About Angles----------?#

#!----------Main----------!#
# Get volume of the parallelepiped of three vectors
def vol_prllp(v1, v2, v3):
	area = np.cross(v1, v2)
	volume = abs(np.inner(area, v3))
	return float(volume)

# Get the unit vector along the given vector
def unit_vector(v):
	return (v/np.linalg.norm(v)).tolist()

# Prolong a vector by a scalar
def prolong(v, s):
	alpha = angle(v, [1,0,0])
	beta = angle(v, [0,1,0])
	gamma = angle(v, [0,0,1])
	increment_x = s * math.cos(alpha)
	increment_y = s * math.cos(beta)
	increment_z = s * math.cos(gamma)
	v_f = []
	v_f.append(round(v[0] + increment_x, 10))
	v_f.append(round(v[1] + increment_y, 10))
	v_f.append(round(v[2] + increment_z, 10))
	return v_f

def prolong_2(v, s):
	norm = np.linalg.norm(v)
	ratio = 1 + s / norm
	v_f = [i*ratio for i in v]
	return v_f

# Find the crossing of a vector and a plane
def crossing(v, p):
	A = p[0][0]
	B = p[0][1]
	C = p[0][2]
	a = p[1][0]
	b = p[1][1]
	c = p[1][2]
	t = sympy.symbols('t')
	f1 = A * (t * v[0] - a) + B * (t * v[1] - b) + C * (t * v[2] - c)
	solution = sympy.solve([f1], [t])
	r = solution[sympy.symbols('t')]
	x = r * v[0]
	y = r * v[1]
	z = r * v[2]
	return [x, y, z]

#?----------Main----------?#
#?-------------------Vectors and scalars--------------------?#

#!--------------------About Coord System (3D)--------------------!#
# Receive a reduced vector and its coord system / Return the Cartesian version
def rd(v, cs):
	cs_transpose = np.transpose(cs)
	x = np.inner(v, cs_transpose[0])
	y = np.inner(v, cs_transpose[1])
	z = np.inner(v, cs_transpose[2])
	return [x, y, z]

# Receive a direct vector and a coord system / Return the reduced version
def dr(v, cs):
	x = sympy.symbols('x')
	y = sympy.symbols('y')
	z = sympy.symbols('z')
	f1 = x * cs[0][0] + y * cs[1][0] + z * cs[2][0] - v[0]
	f2 = x * cs[0][1] + y * cs[1][1] + z * cs[2][1] - v[1]
	f3 = x * cs[0][2] + y * cs[1][2] + z * cs[2][2] - v[2]
	solution = sympy.solve([f1, f2, f3], [x, y, z])
	r1 = solution[sympy.symbols('x')]
	r2 = solution[sympy.symbols('y')]
	r3 = solution[sympy.symbols('z')]
	return [r1, r2, r3]

# Receive a reduced vector, its coord system and a new coord system / Return the reduced vector in the new coord system
def rr(v, cs1, cs2):
	cartesian_temp = rd(v, cs1)
	r_f = dr(cartesian_temp, cs2)
	return r_f
#?--------------------About Coord System (3D)--------------------?#

#!--------------------Rotation--------------------!#
# Receive a point to be rotated, a rotation angle (in degrees CLOCKWISE), the axis (origin, end) and their coord system
# Return the rotated point
def rotate(point, angle, axis_origin, axis_end, cs=[[1,0,0],[0,1,0],[0,0,1]]):
	# Convert the point and the axis to Cartesian version
	point_cartesian = rd(point, cs)
	axis_origin_cartesian = rd(axis_origin, cs)
	axis_end_cartesian = rd(axis_end, cs)
	# Move the axis's origin to (0, 0, 0) and adjust the point accordingly
	point_o = np.array(point_cartesian) - np.array(axis_origin_cartesian)
	axis_o = np.array(axis_end_cartesian) - np.array(axis_origin_cartesian)
	# Shrink the axis to a unit
	axis_o_unit = unit_vector(axis_o)
	# Get the radian version of the rotation angle
	angle_radian = angle / 180 * math.pi
	D = [[axis_o_unit[0]**2+(1-axis_o_unit[0]**2)*math.cos(angle_radian), axis_o_unit[0]*axis_o_unit[1]*(1-math.cos(angle_radian))+axis_o_unit[2]*math.sin(angle_radian), axis_o_unit[0]*axis_o_unit[2]*(1-math.cos(angle_radian))-axis_o_unit[1]*math.sin(angle_radian)],
	     [axis_o_unit[0]*axis_o_unit[1]*(1-math.cos(angle_radian))-axis_o_unit[2]*math.sin(angle_radian), axis_o_unit[1]**2+(1-axis_o_unit[1]**2)*math.cos(angle_radian), axis_o_unit[1]*axis_o_unit[2]*(1-math.cos(angle_radian))+axis_o_unit[0]*math.sin(angle_radian)],
	     [axis_o_unit[0]*axis_o_unit[2]*(1-math.cos(angle_radian))+axis_o_unit[1]*math.sin(angle_radian), axis_o_unit[1]*axis_o_unit[2]*(1-math.cos(angle_radian))-axis_o_unit[0]*math.sin(angle_radian), axis_o_unit[2]**2+(1-axis_o_unit[2]**2)*math.cos(angle_radian)]
	    ]
	# Rotate
	point_temp = np.dot(D, point_o)
	# Move away off (0, 0, 0)
	point_temp = point_temp + np.array(axis_origin_cartesian)
	# Back into the reduced version
	point_temp = dr(point_temp, cs)
	# Format
	point_f = [round(i, 10) for i in point_temp]
	return point_f
#?--------------------Rotation--------------------?#

#!--------------------Miscellaneous--------------------!#
# Generate a random number between a and b; '[' and ']' means closed; '(' and ')' means open.
def rm(a, b, kind='[]'):
	def condition(test):
		if kind == '[]':		
			value = True		
		elif kind == '()':		
			value = test != a and test != b
		elif kind == '(]':
			value = test != a
		elif kind == '[)':
			value = test != b
		return value
	while True:
		random_number = uniform(a, b)
		if condition(random_number):
			break
	return random_number

# Parity determination
def parity(n):
	if number % 2 == 0:
		return 'even'
	elif number % 2 == 1:
		return 'odd'

# Add vacuum
def vacuum(point, cs=[[1,0,0],[0,1,0],[0,0,1]], am=0, ap=0, bm=0, bp=0, cm=0, cp=0):
	a_increment = am + ap
	b_increment = bm + bp
	c_increment = cm + cp
	new_a = prolong(cs[0], a_increment)
	new_b = prolong(cs[1], b_increment)
	new_c = prolong(cs[2], c_increment)

	point_d = rd(point, cs)
	point_vacuum_d = np.array(point_d) + np.array([am, bm, cm])
	point_f = dr(point_vacuum_d, [new_a, new_b, new_c])
	return point_f

# Generate x and f(x) from start to end
def f_l(func, start, end, accuracy=1000000):
	x = []
	for i in range(accuracy + 1):
		x.append(start + i * (end - start) / accuracy)

	y = []
	for i in x:
		y.append(func(i))
	return [x, y]

# Plot a function
def plot_f(func, start, end, accuracy=1000000, color='red', l=''):
	xy = f_l(func, start, end, accuracy)
	x = xy[0]
	y = xy[1]
	plt.plot(x, y, c=color, label=l)

# Fitting - Least Squares Method (y = a + b * x)
def lsm(x, y):
	n = len(x)
	average_x = sum(x) / n
	average_y = sum(y) / n
	sumxiyi = 0
	sumxixi = 0
	for i in range(n):
		sumxiyi += x[i] * y[i]
		sumxixi += x[i] ** 2
	b = (sumxiyi - n * average_x * average_y) / (sumxixi - n * average_x ** 2)
	a = average_y - b * average_x
	return [a, b]

# Find peaks / Return a list containing all peaks; a peak is a list containing x, y and index (python).
def find_peak(x, y):
	peaks = []
	if y[0] > y[1]:
		peak = [x[0], y[0], 0]
		peaks.append(peak)
	length = len(x)
	for i in range(1, length-1):
		if y[i] > y[i-1] and y[i] > y[i+1]:
			peak = [x[i], y[i], i]
			peaks.append(peak)
	if y[-1] > y[-2]:
		peak = [x[-1], y[-1], length-1]
		peaks.append(peak)
	return peaks

# This function finds the very peak and returns the peak location
def fpl(y):
	y_max = max(y)
	for i in range(len(y)):
		if y[i] >= y_max:
			return i

# This function finds the very valley and returns the valley location
def fvl(y):
	y_min = min(y)
	for i in range(len(y)):
		if y[i] <= y_min:
			return i

# Add strain (2D)
# A strain is a list containing two elements: the first element is the magnitude of the strain, the second is the direction in radians
def add_strain(v, strain, vertical_modification=1):
	if strain[1] > math.pi / 2 or strain[1] <= - math.pi / 2:
		print("Your strain direction should not exceed the range (-pi/2 , pi/2]")
	else:
		if strain[1] == 0:
			x = v[0] * strain[0]
			y = v[1] * vertical_modification
			z = v[2]
		elif strain[1] == math.pi / 2:
			x = v[0] * vertical_modification
			y = v[1] * strain[0]
			z = v[2]
		else:
			slope = math.tan(strain[1])
			strain_parallel = [1, slope, 0]
			strain_vertical = rotate(strain_parallel, 270, [0,0,0], [0,0,1])
			v_strain_coord = dr(v, [strain_parallel, strain_vertical, [0,0,1]])
			v_strain_coord[0] = v_strain_coord[0] * strain[0]
			v_strain_coord[1] = v_strain_coord[1] * vertical_modification
			strained_v = rd(v_strain_coord, [strain_parallel, strain_vertical, [0,0,1]])
			x = strained_v[0]
			y = strained_v[1]
			z = strained_v[2]
		v_f = [x, y, z]
		return 

# Project a vector v1 to the other vector v2
def proj(v1, v2):
	projection = np.inner(v1, v2) / np.linalg.norm(v2)
	return projection

# Sort x list from small to large, and adjust y list corresponding to x
def sort_xy(x, y):
	length = len(x)
	counters = []
	for i in range(length):
		counter = 0
		for j in range(length):
			if x[i] > x[j]:
				counter += 1
			elif x[i] == x[j]:
				if i > j:
					counter +=1
		counters.append(counter)

	new_x = []
	new_y = []
	for i in range(length):
		new_x.append(x[counters.index(i)])
		new_y.append(y[counters.index(i)])

	return [new_x, new_y]

# Convert index from human-readable to python
def ihp(index):
	if index > 0:
		index = index - 1
	return index

# Merge int, float & str together
def auto_type(operand, data_type=''):
	if data_type == 'int':
		operand_f = int(operand)
	elif data_type == 'float':
		operand_f = float(operand)
	elif data_type == 'str':
		operand_f = str(operand)
	else:
		operand_f = operand
	return operand_f

# This function returns specified number of spaces
def spaces(number):
	msg = ''
	for i in range(number):
		msg += ' '
	return msg
#?--------------------Miscellaneous--------------------?#

#!--------------------Lists--------------------!#
# Format a list
# WARNING! It omits float number even when you specify data_type is 'int', i.e. it won't convert a float number to an integer
def format_l(ls, data_type):
	ls_f = []
	for i in ls:
		try:
			ls_f.append(auto_type(i, data_type))
		except ValueError:
			continue
	return ls_f

# Convert a list to a line
def lsl(ls, space_number=1):
	msg = ''
	for i in ls:
		msg += str(i)
		msg += spaces(space_number)
	if space_number != 0:
		msg = msg[:-space_number]
	return msg

# This function turns all numbers to their absolute values
def absl(x):
	return [abs(i) for i in x]

# Find value's index 
def index_v2(ls, value, occurrence=1):
	for i in range(occurrence-1):
		ls.remove(value)
	index = ls.index(value)
	return index + occurrence - 1
#?--------------------Lists--------------------?#

#!--------------------Lines--------------------!#
# Convert a line to a list based on spaces
def lls(line, data_type=''):
	return format_l(line.split(), data_type)

# Remove specified characters from the string
def cleanse(string, character):
	ls = list(string)
	number = ls.count(character)
	for i in range(number):
		ls.remove(character)
	clean_string = lsl(ls, 0)

	return clean_string

# Remove the first character that matches the specified characters
def remove_character_first(string, characters):
	temp_list = list(string)
	for i in characters:
		if i in temp_list:
			temp_list.remove(i)
	new_string = ''
	for i in temp_list:
		new_string += i
	return new_string

# Add a character before index (human-readable); and another character after index in a string
def squeeze(string, index, c1, c2):
	ls = list(string)
	ls.insert(index-1, c1)
	ls.insert(index+1, c2)
	new_string = lsl(ls, 0)
	return new_string
#?--------------------Lines--------------------?#

#!--------------------Files--------------------!#
# Convert a text file to lines
def line(filename):
	with open(filename) as f:
		lines = f.readlines()
	lines_striped = [line.rstrip() for line in lines]
	return lines_striped

# Get the number of rows in a file
def rn(filename):
	return len(line(filename))

# Get the element at specified row and column in a file
def rc(filename, row, column):
	lines = line(filename)
	row_index = ihp(row)
	column_index = ihp(column)
	target_row = lines[row_index].split()
	target = target_row[column_index]
	return target

# Get a specified column in a file
def col(filename, column_number, row_start=1, row_end=0, data_type=''):
	lines = line(filename)
	total_rows = len(lines)
	if row_end == 0:
		row_end = total_rows
	lines_f = []
	for i in lines:
		lines_f.append(lls(i, data_type))
	x = []
	try:
		for i in range(row_start, row_end+1):
			x.append(lines_f[i-1][column_number-1])
	except IndexError:
		print('Check the length of your lists! ')

	return x

# Get two columns in a file
def col2(filename, column_1, column_2, row_start=1, row_end=0, data_type=''):
	x = col(filename, column_1, row_start, row_end, data_type)
	y = col(filename, column_2, row_start, row_end, data_type)
	return [x, y]

# This function reads several lines and returns a list of replaced lines
def find_replace_textfile(lines, string_pairs):
	# string_pairs contains many string_pairs
	# each string_pair is a list;
	# the first element is a 'mode'; mode = 0: search all lines; mode = 1(or 2, 3, ... or a list containing many line serial number): search specified line
	# the second element in each string_pair list is the old_string which is to be replaced; 
	# the third element is the new_string which is to be replaced with. 
	for string_pair in string_pairs:
		if string_pair[0] == 0:
			for serial_number in range(len(lines)):
				lines[serial_number] = lines[serial_number].replace(string_pair[1], string_pair[2])
		elif type(string_pair[0]) == int:
			lines[string_pair[0]-1] = lines[string_pair[0]-1].replace(string_pair[1], string_pair[2])
		elif type(string_pair[0]) == list:
			for serial_number in string_pair[0]:
				lines[serial_number-1] = lines[serial_number-1].replace(string_pair[1], string_pair[2])

	return lines
#?--------------------Files--------------------?#

#!--------------------Directories--------------------!#
# This function returns all folders needed in a specified folder by the parameter 'folder'
def listrealdir(folder='.'):
	raw_folders = os.listdir(folder)    # raw_folders contains many elements that might be a folder which I don't need
	raw_folders.sort()
	folders = []
	for i in raw_folders:
		if i != '.':
			if os.path.isdir(folder + '/' + i):
				folders.append(i)
	return folders
#?--------------------Directories--------------------?#