import random
import math
import numpy
import matplotlib.pyplot as plt

DEBUG = False
DEBUG_VERBOSE = False

def main():
	t = 0 # t -> time
	dt = 0.1 # delta t -> change of t every time
	T = 300.0 # speed of particle (Temperature, in Kelvin)
	d = 10 ** (-9) # distance threshold
	k = 1.38 * 10 ** (-23)
	mx = 2.66 * 10 ** (-26) # two masses
	my = 2.82 * 10 ** (-26) # two masses
	P = 10.0 ** 5
	V = 1.0 * 10 ** (-3) # volume
	nx = P * V / k / T / 2 # some magic value
	ny = P * V / k / T / 2
	n = nx + ny
	nz = 0.0
	nw = 0.0
	trials = 10 ** 4 # trials
	sideLength = 0.3 * 10 ** (-8)
	E = math.sqrt(T * k / mx) ** 2 * mx # reaction energy
	data = []
	#reactions = 0.0
	
	class Recorder:
		def __init__(self):
			self.recdata = []
		
		def add(self, var_name, var_value):
			self.recdata.append((var_name, var_value))
		
		def get(self, var_name):
			return [var[1] for var in self.recdata if var[0] == var_name]
		
		def plot(self, scatter: bool, *keys):
			if len(keys) == 2:
				plt.clf()
				x, y = self.get(keys[0]), self.get(keys[1])
				# print(x, y)
				if scatter:
					plt.scatter(x, y)
				else:
					plt.plot(x, y)
				plt.show()
			else:
				raise ValueError("Plot Keys should be exactly two.")
	
	record = Recorder()
	
	def transform(data):
		x, y = [], []
		for dx, dy in data:
			x.append(dx)
			y.append(dy)
		return x, y
	
	while t < 2:
		data += [[t, nz]]
		pnx = nx / n
		pny = ny / n
		pnz = nz / n
		pnw = nw / n
		reactions = 0.0
		for n in range(trials):
			reactionWillHappen = False
			random1 = random.random()
			random2 = random.random()
			record.add("random1|2", f"{random1}|{random2}")
			if (random1 < pnx and random2 > 1 - pny) or (random2 < pnx and random1 > 1 - pny):
				#print("right particles, simulate reaction")
				reactionWillHappen = True
				x1 = sideLength * random.random()
				y1 = sideLength * random.random()
				z1 = sideLength * random.random()
				x2 = sideLength * random.random()
				y2 = sideLength * random.random()
				z2 = sideLength * random.random()
				record.add("x1", x1)
				record.add("x2", x2)
				record.add("y1", y1)
				record.add("y2", y2)
				record.add("z1", z1)
				record.add("z2", z2)
				if random1 < pnx: # close enough?
					m1 = mx # do nothing
					m2 = my
				else:
					m2 = mx
					m1 = my
				vx1 = math.sqrt(k * T / m1) * numpy.random.normal(0, 1)
				vy1 = math.sqrt(k * T / m1) * numpy.random.normal(0, 1)
				vz1 = math.sqrt(k * T / m1) * numpy.random.normal(0, 1)
				vx2 = math.sqrt(k * T / m2) * numpy.random.normal(0, 1)
				vy2 = math.sqrt(k * T / m2) * numpy.random.normal(0, 1)
				vz2 = math.sqrt(k * T / m2) * numpy.random.normal(0, 1)
				if (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 > d ** 2:
					record.add("stats_err_distfar", True)
					if DEBUG:
						if DEBUG_VERBOSE:
							print(f"[=] TOO FAR. distance ({(x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2}) is greater than threshold ({d ** 2})")
						else:
							print(f"[=] [t = {round(t, 2)}] TOO FAR.")
					reactionWillHappen = False
				else:
					record.add("stats_ok_distfar", True)
				if reactionWillHappen:
					vxcm = (m1 * vx1 + m2 * vx2) / (m1 + m2)
					vycm = (m1 * vy1 + m2 * vy2) / (m1 + m2)
					vzcm = (m1 * vz1 + m2 * vz2) / (m1 + m2)
					KEcm = 1 / 2 * m1 ** ((vx1 - vxcm) ** 2 + (vy1 - vycm) ** 2 + (vz1 - vzcm) ** 2) + 1 / 2 * m2 ** ((vx2 - vxcm) ** 2 + (vy2 - vycm) ** 2 + (vz2 - vzcm) ** 2)
					record.add("vxcm", vxcm)
					record.add("vycm", vycm)
					record.add("vzcm", vzcm)
					record.add("KEcm", KEcm)
					if KEcm < E:
						record.add("stats_err_noenergy", True)
						reactionWillHappen = False
						if DEBUG:
							if DEBUG_VERBOSE:
								print(f"[-] NOT ENOUGH ENERGY. Particle at {t}s with: (vxcm {vxcm}), (vycm {vycm}), (vzcm {vzcm}), (KEcm {KEcm})")
							else:
								print(f"[-] [t = {round(t, 2)}] NOT ENOUGH ENERGY.")
					if reactionWillHappen:
						reactions += 1.0
						print(f"[+] [t = {round(t, 2)}] #{int(reactions)} REACTION HAPPENED at {t}s, with: (vxcm {vxcm}), (vycm {vycm}), (vzcm {vzcm}), (KEcm {KEcm})")
					pass
				pass
			pass
		nx = nx - reactions / trials * n * (n - 1) * (sideLength ** 3 / V)
		ny = ny - reactions / trials * n * (n - 1) * (sideLength ** 3 / V)
		nz = nz - reactions / trials * n * (n - 1) * (sideLength ** 3 / V)
		t += dt
		# print(f"[t {t}] reactions {reactions}, trials {trials}, n {n}")
		
	print(numpy.array(data))
	
	print("Calculating Diagnostic Data...")
	
	print(f'Diagnostics of testing ({len(record.get("random1|2"))}):')
	print(f'\tNot Reacting ({len(record.get("stats_err_noenergy")) + len(record.get("stats_err_distfar"))}) ({(len(record.get("stats_err_noenergy")) + len(record.get("stats_err_distfar"))) / len(record.get("random1|2"))*100}%):')
	print(f'\t\tDistance Too Far: {len(record.get("stats_err_distfar"))} ({round(100*(len(record.get("stats_err_distfar")) / (len(record.get("stats_err_noenergy")) + len(record.get("stats_err_distfar")))), 3)}%)')
	print(f'\t\tEnergy Not Enough: {len(record.get("stats_err_noenergy"))} ({round(100*(len(record.get("stats_err_noenergy")) / (len(record.get("stats_err_noenergy")) + len(record.get("stats_err_distfar")))), 3)}%)')

if __name__ == '__main__':
	for _ in range(5):
		main()

'''
plt.plot(*transform(x, y))
plt.show()
'''

'''
plt.clf()
randoms = [a.split("|") for a in record.get("random1|2")]
plt.scatter(*transform(randoms))
plt.show()
'''

'''
record.plot(True, "x1", "x2")
record.plot(True, "y1", "y2")
record.plot(True, "z1", "z2")
'''
