NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

class Robot(object):
	def __init__(self, bearing=NORTH, x=0, y=0):
		self.bearing = bearing
		self.coordinates = (x, y)

	def turn_left(self):
		self.bearing = (self.bearing - 1) % 4

	def turn_right(self):
		self.bearing = (self.bearing + 1) % 4

	def advance(self):
		movements = {
			NORTH: lambda x,y: (x, y+1),
			EAST:  lambda x,y: (x+1, y),
			SOUTH: lambda x,y: (x, y-1),
			WEST:  lambda x,y: (x-1, y),
		}
		x, y = self.coordinates
		self.coordinates = movements[self.bearing](x,y)

	def simulate(self, programming):
		funcs = {
			'R': self.turn_right,
			'L': self.turn_left,
			'A': self.advance
		}
		
		for instruction in programming:
			funcs[instruction]()