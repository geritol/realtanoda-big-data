import math
import random
import numpy as np
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
