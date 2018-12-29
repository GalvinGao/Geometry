import math
import random
import matplotlib.pyplot as plt
import numpy

DEBUG = False  # output the summary of a timeframe
DEBUG_VERBOSE = False  # output each trial's result in a period of time

t = 0  # t -> time
dt = .01  # delta t -> change of t every time
totaltime = 20 # run for ? seconds
T = 300.0  # speed of particle (Temperature, in Kelvin)
d = 10 ** (-9)  # distance threshold
k = 1.38 * 10 ** (-23)  # boltzmann constant
mx = 1 * 10 ** (-22)  # two masses
my = 2 * 10 ** (-22)  # two masses
P = 10.0 ** 5  # air pressure
V = 1.0 * 10 ** (-3)  # volume
nx = P * V / k / T / 2  # ideal gas law
ny = P * V / k / T / 2  # ideal gas law
nz = 0.0
nw = 0.0
n = nx + ny + nz + nw
trials = 10 ** 5  # trials
sideLength = 10 ** (-8)  # side length of the box
E = math.sqrt(T * k / mx) ** 2 * mx  # reaction energy
data = []


# reactions = 0.0

# store the progress of the calculation
class Recorder:
	def __init__(self):
		self.recdata = []
		
	def add(self, var_name, var_value):
		self.recdata.append((var_name, var_value))
		
	def get(self, var_name):
		return [var[1] for var in self.recdata if var[0] == var_name]
		
	def plot(self, scatter: bool, *keys: str):
		if len(keys) == 1:
			plt.clf()
			x, y = range(len(self.get(keys[0]))), self.get(keys[0])
			# print(x, y)
			plt.title(f"function of trials and {keys[0]}")
			plt.xlabel("areas index")
			plt.ylabel(f"Value of {keys[0]}")
			if scatter:
				plt.scatter(x, y)
			else:
				plt.plot(x, y)
			plt.show()
		elif len(keys) == 2:
			plt.clf()
			x, y = self.get(keys[0]), self.get(keys[1])
			# print(x, y)
			plt.xlabel(f"Value of {keys[0]}")
			plt.ylabel(f"Value of {keys[1]}")
			plt.title(f"function of {keys[0]} and {keys[1]}")
			if scatter:
				plt.scatter(x, y)
			else:
				plt.plot(x, y)
			plt.show()
		else:
			raise ValueError("Plot Keys should be exactly two.")

# store the progress of the calculation; optimized with dict
class OptimizedRecorder:
	def __init__(self):
		self.recdata = {}
		
	def add(self, var_name, var_value):
		if var_name in self.recdata:
			self.recdata[var_name].append(var_value)
		else:
			self.recdata[var_name] = [var_value]
		
	def get(self, var_name):
		return self.recdata.get(var_name)
		
	def plot(self, scatter: bool, *keys: str):
		if len(keys) == 1:
			plt.clf()
			x, y = range(len(self.get(keys[0]))), self.get(keys[0])
			# print(x, y)
			plt.title(f"function of trials and {keys[0]}")
			plt.xlabel("areas index")
			plt.ylabel(f"Value of {keys[0]}")
			if scatter:
				plt.scatter(x, y)
			else:
				plt.plot(x, y)
			plt.show()
		elif len(keys) == 2:
			plt.clf()
			x, y = self.get(keys[0]), self.get(keys[1])
			# print(x, y)
			plt.xlabel(f"Value of {keys[0]}")
			plt.ylabel(f"Value of {keys[1]}")
			plt.title(f"function of {keys[0]} and {keys[1]}")
			if scatter:
				plt.scatter(x, y)
			else:
				plt.plot(x, y)
			plt.show()
		else:
			raise ValueError("Plot Keys should be exactly two.")
			
# store the stats of the simulation
class Incrementor():
	def __init__(self):
		self.recdata = {}
	
	def add(self, rec_key, rec_val: int = 1):
		if rec_key in self.recdata:
			self.recdata[rec_key] += rec_val
		else:
			self.recdata[rec_key] = rec_val
	
	def get(self, rec_key):
		return self.recdata.get(rec_key)

# store nothing
class FakeRecorder():
	def __init__(self):
		pass
	
	def get(self, *_, **__):
		pass
	
	def set(self, *_, **__):
		pass
	
	def add(self, *_, **__):
		pass
	
	def plot(self, *_, **__):
		pass

record = FakeRecorder()
incrementor = Incrementor()


def transform(data):
	x, y = [], []
	for dx, dy in data:
		x.append(dx)
		y.append(dy)
	return x, y
	
	
while t < totaltime:
	data += [[t, nz]]
	pnx = nx / n
	pny = ny / n
	pnz = nz / n
	pnw = nw / n
	reactions = 0.0
	for _ in range(trials):
		reactionWillHappen = True
		random1 = random.random()
		random2 = random.random()
		incrementor.add("tries")
		if (random1 < pnx and random2 > 1 - pny) or (random2 < pnx and random1 > 1 - pny):
			# print("right particles, simulate reaction")
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
			if random1 < pnx:  # close enough?
				m1 = mx  # do nothing
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
		else:
			reactionWillHappen = False
			continue
			
		# Condition 1: Check the distance
		if (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 > d ** 2:
			incrementor.add("stats_err_distfar")
			if DEBUG:
				if DEBUG_VERBOSE:
					print(
					f"[=] TOO FAR. distance ({(x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2}) is greater than threshold ({d ** 2})")
				else:
					print(f"[=] [t = {round(t, 2)}] TOO FAR.")
			reactionWillHappen = False
			continue
		else:
			incrementor.add("stats_ok_distfar")
		vxcm = (m1 * vx1 + m2 * vx2) / (m1 + m2)
		vycm = (m1 * vy1 + m2 * vy2) / (m1 + m2)
		vzcm = (m1 * vz1 + m2 * vz2) / (m1 + m2)
		KEcm = 1 / 2 * m1 ** ((vx1 - vxcm) ** 2 + (vy1 - vycm) ** 2 + (vz1 - vzcm) ** 2) + 1 / 2 * m2 ** (
		(vx2 - vxcm) ** 2 + (vy2 - vycm) ** 2 + (vz2 - vzcm) ** 2)
		record.add("vxcm", vxcm)
		record.add("vycm", vycm)
		record.add("vzcm", vzcm)
		record.add("KEcm", KEcm)
		# Condition 2: Check the energy
		if KEcm < E:
			incrementor.add("stats_err_noenergy")
			reactionWillHappen = False
			if DEBUG:
				if DEBUG_VERBOSE:
					print(
					f"[-] [t = {round(t, 2)}] NOT ENOUGH ENERGY. Particle with: (vxcm {vxcm}), (vycm {vycm}), (vzcm {vzcm}), (KEcm {KEcm})")
				else:
					print(f"[-] [t = {round(t, 2)}] NOT ENOUGH ENERGY.")
		else:
			incrementor.add("stats_ok_reacted")
			reactions += 1.0
			print(
			f"[+] [t = {round(t, 2)}] #{int(reactions)} REACTION HAPPENED, with: (vxcm {vxcm}), (vycm {vycm}), (vzcm {vzcm}), (KEcm {KEcm})")
		pass
	nx = nx - reactions / trials * n * (n - 1) * (sideLength ** 3 / V)
	ny = ny - reactions / trials * n * (n - 1) * (sideLength ** 3 / V)
	nz = nz + reactions / trials * n * (n - 1) * (sideLength ** 3 / V)
	record.add("nx", nx)
	record.add("ny", ny)
	record.add("nz", nz)
	t += dt
	record.add("t", t)
# print(f"[t {t}] reactions {reactions}, trials {trials}, n {n}")

print(numpy.array(data))

def plot(logrithmic: bool, name: str="", *data):
	if len(data) == 0:
		raise ValueError("No data field.")
	elif len(data) == 1:
		tdata = data[0]
		plt.clf()
		plt.plot(range(len(tdata)), tdata)
		plt.grid(True)
		plt.title(f"function of {name}")
		plt.xlabel(name.split(" and ")[0])
		plt.ylabel(name.split(" and ")[1])
		if logrithmic:
			plt.yscale('log')
		plt.show()
	elif len(data) == 2:
		plt.clf()
		plt.plot(*data, 'b.')
		plt.grid(True)
		plt.title(f"function of {name}")
		plt.ylim(48, 54)
		plt.xlabel(name.split(" and ")[0])
		plt.ylabel(name.split(" and ")[1])
		if logrithmic:
			plt.yscale('log')
		plt.show()
	else:
		raise ValueError(f"data dimension not recognized. (data len: {len(data)}, first data dimension: {len(data[0])})")

plt.plot(*transform(data))
plt.show()

t = record.get("t")
nxs = record.get("nx")
y = []
for i in range(1, len(nxs) - 1):
	dxdt = 0.5 * ((nxs[i] + nxs[i-1]) / (t[i] - t[i-1]) + (nxs[i+1] - nxs[i]) / (t[i+1] - t[i]))
	y.append(dxdt)

x = [math.log(xx) for xx in nxs[2:]]
y = [math.log(abs(yy)) for yy in y]
plot(False, "ln_nx and ln_dxdt", x, y)


'''
print("Calculating Diagnostic Data...")

print(f'Diagnostics of testing ({len(record.get("tries"))}):')
print(
    f'\tNot Reacting ({incrementor.get("stats_err_noenergy") + incrementor.get("stats_err_distfar")}) ({(incrementor.get("stats_err_noenergy") + incrementor.get("stats_err_distfar")) / incrementor.get("tries")*100}%):')
print(
    f'\t\tDistance Too Far: {incrementor.get("stats_err_distfar"))} ({round(100*(incrementor.get("stats_err_distfar")) / (incrementor.get("stats_err_noenergy")) + incrementor.get("stats_err_distfar")))), 3)}%)')
print(
    f'\t\tEnergy Not Enough: {incrementor.get("stats_err_noenergy"))} ({round(100*(incrementor.get("stats_err_noenergy")) / (incrementor.get("stats_err_noenergy")) + incrementor.get("stats_err_distfar")))), 3)}%)')
print(
    f'\tReacting ({incrementor.get("stats_ok_reacted"))}) ({round(incrementor.get("stats_ok_reacted")) / incrementor.get("tries"))*100, 3)}%)')
print(
    f'\tCondition Not Matched ({incrementor.get("tries")) - (incrementor.get("stats_ok_reacted")) + incrementor.get("stats_err_noenergy")) + incrementor.get("stats_err_distfar")))}) ({round((incrementor.get("tries")) - (incrementor.get("stats_ok_reacted")) + incrementor.get("stats_err_noenergy")) + incrementor.get("stats_err_distfar")))) / incrementor.get("tries"))*100, 3)}%)')
'''

'''
plt.clf()
randoms = [a.split("|") for a in record.get("tries")]
plt.scatter(*transform(randoms))
plt.show()
'''

'''
record.plot(True, "x1", "x2")
record.plot(True, "y1", "y2")
record.plot(True, "z1", "z2")
'''

