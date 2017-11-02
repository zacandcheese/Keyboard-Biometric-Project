import numpy as np
import matplotlib.pyplot as plt
import glob, os
from itertools import cycle

os.chdir("/Users/zacan/OneDrive/Documents/GitHub/Keyboard-Biometric-Testing/library")

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	#print(file)
	try:
		np.loadtxt(file, delimiter=",", unpack=True)
		listOfTxtFiles.append(file)
	except ValueError:
		pass


lines = ["-","--","-.",":"]
linecycler = cycle(lines)
for i in range(len(listOfTxtFiles)):
	plt.figure("PRESS TIME")
	array = np.loadtxt(listOfTxtFiles[i], delimiter=",", unpack=True)
	plt.plot(array[0][3:], array[2][3:], next(linecycler), label = listOfTxtFiles[i])
plt.legend()
plt.show()

for i in range(len(listOfTxtFiles)):
	plt.figure("FLIGHT TIME")
	array = np.loadtxt(listOfTxtFiles[i], delimiter=",", unpack=True)
	plt.plot(array[0][3:], array[3][3:], lines[0], label = listOfTxtFiles[i])
plt.legend()
plt.show()