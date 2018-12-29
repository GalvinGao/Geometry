import math
import matplotlib.pyplot as plt


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
			
			
record = Recorder()

a0 = 5.29177 * 10 ** (-11)
rmax = 10 * a0
areas = 100

sumValue = 0

for n in range(areas):
	tempR = n * rmax / areas
	psi = 2.0 / (a0 ** (1.5)) * math.exp(-tempR / a0)
	# tempR = n * rmax / areas
	tempA = psi ** 2 * tempR ** 2 * rmax / areas
	sumValue = sumValue + tempR * tempA
	record.add("tempR", tempR)
	record.add("psi", psi)
	record.add("tempA", tempA)
	record.add("sumValue", sumValue)
print(sumValue)

record.plot(False, "tempR")
record.plot(False, "psi")
record.plot(False, "tempA")
plt.clf()
plt.plot(range(len(record.get("psi"))), [x * record.get("tempR")[ind] for ind, x in enumerate(record.get("psi"))])
plt.plot(range(len(record.get("psi"))), [x ** 2 * record.get("tempR")[ind] ** 2 for ind, x in enumerate(record.get("psi"))])
plt.plot(range(len(record.get("psi"))), [x ** 2 * record.get("tempR")[ind] ** 2 * rmax for ind, x in enumerate(record.get("psi"))])
plt.show()
record.plot(False, "sumValue")
