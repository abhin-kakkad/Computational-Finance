import numpy as np;
import matplotlib.pyplot as plt

array = np.zeros(101);
array2 = np.zeros((1,101));

for i in range(0,101):
	array2[0,i]  =i;

n = 10000;
count =0;
sum =0;

#Maximum Function
def max(a,b):
	if a>b:
		return a
	else:
		return b

for i in range(1,n):	
	sum =0;
	for j in range(1,101):
		a = np.random.randint(2);
		if a==0:
			sum = sum-1;
		else:
			sum =sum+1;
		if sum==0:
			p = j;
	array[p] = array[p]+ 1;

array2  = np.arange(0,101,1);

#Generating the Bar Graph
plt.bar(array2,array,align='center');	
plt.ylabel('Density')
plt.xlabel('Time Step')
plt.show()	
