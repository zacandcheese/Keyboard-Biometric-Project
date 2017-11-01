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
	plt.figure(1)
	array = np.loadtxt(listOfTxtFiles[i], delimiter=",", unpack=True)
	plt.plot(array[0], array[2], next(linecycler), label = listOfTxtFiles[i])# array[0], array[4], 'ro' USE FOR AVG FLIGHT TIME
plt.legend()
plt.show()