import math
import random
import numpy as np
import pylab as plt

pi = math.pi
#
# tower_x = 46.971740
# tower_y = 21.087803
tower_x = 47.513853
tower_y = 19.0542355
r = 35/111.3



# positions = []
#
# x = []
# y = []
#
# for i in range(1000):
# 	q = random.random() * (pi * 2)
# 	r = random.random() ** 2
# 	x.append((radius * r) * math.cos(q))
# 	y.append((radius * r) * math.sin(q))
#
# x0 = np.median(x)
# y0 = np.median(y)
# r = np.sqrt((x - x0)**2 + (y - y0)**2)
# r0 = np.percentile(r, 100)
#
#




x = []
y = []

# for i in range(1000):
# 	t = 2 * pi * random.random()
# 	u = random.random() + random.random()
# 	r = 2 - u if u > 1 else u
# 	x.append(r*math.cos(t))
# 	y.append(r*math.sin(t))
#
# print(x)
# print(y)


def randomCoords(r, x0, y0):

	u = random.random()
	v = random.random()

	w = r * math.sqrt(u)
	t = 2 * pi * v

	x = w * math.cos(t)
	y = w * math.sin(t)

	_x = x / math.cos(y0)

	return [_x + x0, y + y0]

# xs = []
# ys = []
#
# for i in range(1000):
# 	coord = randomCoords(r, tower_x, tower_y)
# 	xs.append(coord[0])
# 	ys.append(coord[1])
#