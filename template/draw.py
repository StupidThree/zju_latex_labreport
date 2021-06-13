from math import *
import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
#plt.figure(figsize=(10,6))

def f(x):
	t=floor(x/0.5)
	if int(t)%2==0:
		return -0.25
	return 0.25

def g(x):
	t=floor(x/0.5)
	if int(t)%2==0:
		return 0.2-0.8*(x-t*0.5)
	return -0.2+0.8*(x-t*0.5)

x,y,a,b=[],[],[],[]
for i in range(0,1000):
	xx=i*0.01
	x.append(xx)
	y.append(-10*f(xx)-10*g(xx))
	a.append(f(xx))
	b.append(g(xx))

textsize=15

plt.plot(x,y)

plt.xlabel('t/ms',fontsize=textsize)
plt.ylabel('U/V',fontsize=textsize)
plt.xticks(fontsize=textsize)
plt.yticks(fontsize=textsize)

plt.grid()

#plt.xticks(np.arange(-10,11,1))
#plt.yticks(np.arange(880,1421,60))
plt.show()