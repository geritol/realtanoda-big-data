import math
import random
import pylab as plt

pi = math.pi


def randomCoords(r, x0, y0):

	u = random.random()
	v = random.random()

	w = r * math.sqrt(u)
	t = 2 * pi * v

	x = w * math.cos(t)
	y = w * math.sin(t)

	_x = x / math.cos(y0)

	return [_x + x0, y + y0]
 
#tower_x = 47.513853
#tower_y = 19.0542355
#r = 35/111.3
#
#xs = []
#ys = []
#
#for i in range(1000):
#	coord = randomCoords(r, tower_x, tower_y)
#	xs.append(coord[0])
#	ys.append(coord[1])
#
#plt.plot(xs, ys, '.')
#circle = plt.Circle((tower_x, tower_y), r, color='r', fill=False)
#
#plt.show()