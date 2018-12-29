import matplotlib.pyplot as plt
import numpy as np
import math

V = 1.0 * 10 ** (-3)  # volume
k = 1.38 * 10 ** (-23) # the magic constant! whohoo!

def get_data(key):
	file = open(f".save/save-{key}.data", "r", encoding="utf8")
	result = eval(file.read())
	file.close()
	return result

def transform(data):
	x, y = [], []
	for dx, dy in data:
		x.append(dx)
		y.append(dy)
	return x, y

def plot(logrithmic: bool, name: str="", ylim: tuple = None, *data):
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
		plt.plot(*data)
		plt.grid(True)
		plt.title(f"function of {name}")
		if ylim:
			plt.ylim(*ylim)
		plt.xlabel(name.split(" and ")[0])
		plt.ylabel(name.split(" and ")[1])
		if logrithmic:
			plt.yscale('log')
		plt.show()
	else:
		raise ValueError(f"data dimension not recognized. (data len: {len(data)}, first data dimension: {len(data[0])})")

def plot_data(log, *keys):
	results = [get_data(key) for key in keys]
	plot(log, " and ".join(keys), *results)

# plot_data(False, "t", "nz")

nxs = get_data("nx")
nzs = get_data("nz")
concentration = []
for nx in nxs:
	result = (nx / V) / (6.022 * 1e23) / 1000
	concentration.append(result)

t = get_data("t")
y = []
for i in range(1, len(nxs) - 1):
	dxdt = 0.5 * ((nxs[i] + nxs[i-1]) / (t[i] - t[i-1]) + (nxs[i+1] - nxs[i]) / (t[i+1] - t[i]))
	y.append(dxdt)

x = [math.log(xx) for xx in nxs[2:]]
y = [math.log(abs(yy)) for yy in y]
plot(False, "ln_nx and ln_dxdt", (49, 54), x, y)
fit = np.polyfit(x, y, 1)
print(f"best fit line: y = {fit[0]}x + {fit[1]}")
print('==='*20)
#print('\n'*15)
plt.clf()
plt.plot(t, nzs)
fit2 = np.polyfit(t, nzs, 2)
plt.plot(np.unique(t), np.poly1d(fit2)(np.unique(t)), 'r-.')
plt.show()
print(f"best fit line coeff: {fit2}")
# plot_data(False, "t", "nz")

