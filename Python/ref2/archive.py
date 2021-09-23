# np.trapz(y, x)
def get_definite_integral(x, y):
	point_number = len(x)
	heights = []
	for i in range(point_number-1):
		height = (y[i] + y[i+1]) / 2
		heights.append(height)
	bases = []
	for i in range(point_number-1):
		base = x[i+1] - x[i]
		bases.append(base)
	areas = []
	for i in range(point_number-1):
		area = heights[i] * bases[i]
		areas.append(area)
	result = sum(areas)
	return result
