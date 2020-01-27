from matplotlib import pyplot as plt 
import numpy as np 
v1=int(input("enter a number"))
v2=int(input("enter another number"))
age=np.arange(v1,v2)
weight=age+(age*0.2)
plt.plot(age,weight)
plt.show()