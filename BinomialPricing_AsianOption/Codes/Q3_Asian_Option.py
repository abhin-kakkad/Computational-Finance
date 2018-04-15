import math
import array

def binomial(S0,u,d,n):
	stkval=[]
	for i in range(n+1):
		stkval.append([]) 
		if i==0:
			stkval[i].append(S0)
			continue  
		for j in range(0,2**(i-1)):
			stkval[i].append(stkval[i-1][j]*u)
			stkval[i].append(stkval[i-1][j]*d)
	return stkval

K=2
u=2.0
d=0.5
S0=4.0
k=4

q=binomial(S0,u,d,K)

optval=q
r=.25
mu=(1+r-d)/(u-d)
sigma=1-mu


optval=q

for i in range(0,(2**K)):
	optval[K][i]=q[K][i]
	power=2
	for j in range(1,K+1):
		ind=K-j
		optval[K][i]=optval[K][i]+q[ind][i//(power)]
		power=power*2
	optval[K][i]=max((optval[K][i])/(K+1)-k,0.0)

for i in range(1,K+1):
	ind=K-i
	for j in range(0,len(q[ind])):
			z=(optval[ind+1][j*2]*mu)+(optval[ind+1][j*2+1]*sigma)
			z=z/(1+r)
			optval[ind][j]=z

print ("Asian Option Price at time t=0 :",optval[0][0])
