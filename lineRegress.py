from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
x = np.random.random(10)
x = sorted(x)
y = np.random.random(10)
y = sorted(y)
slope, intercept, r_value,p_value,std_err = stats.linregress(x,y)
plt.plot(x, y)
plt.show()
print(slope)
print(r_value)
p = np.polyfit(x,y,2)
print(p)
a = np.array([[1,2,3,4,5],[2,4,8,16,32]])
b = np.array([[1,2,3,4,5],[1,1,1,1,1]])

def corr2_coeff(A, B):
	A_mA = A - A.mean(1)[:,None]
	B_mB = B - B.mean(1)[:,None]
	
	ssA = (A_mA**2).sum(1)
	ssB = (B_mB**2).sum(1)
	return np.dot(A_mA,B_mB.T)/np.sqrt(np.dot(ssA[:,None],ssB[None]))
	
print(corr2_coeff(a,b))