import numpy as np

#Function to find the larger number between two numbers
def max(a,b):
	if a>=b:
		return a
	else:
		return b


#k : Strike Price
#u : Price of option if it goes up
#d : Price of option if it goes down
#r : Risk Free Interest Rate 
#n : Number of coin tosses

n=5
k=3
u=1.5
d=0.8
r=0.25

stockprice=np.zeros((n,n))

for i in range (0,n):
	s=1
	for j in range(0,n-i-1):
		s=s*u
	for k in range(n-i,n):
		s=s*d
	stockprice[i,n-1]=max(s-k,0)

	
p = (1+r-d)/float(u-d)
q = 1 - p;

for i in range(2,n+1):
	for j in range(0,n-i+1):
		stockprice[j,n-i] = (p*stockprice[j,n-i+1] + q*stockprice[j+1,n-i+1])/float(1+r)

print("European call option price at time t=0:")
print(stockprice[0,0])	
