import numpy as np
import matplotlib.pyplot as plt

#constants
N = 64.0 #divisions for the calculation / increment in step size

#Brownian Motion
def Brownian(seed, N):
    
    np.random.seed(seed)
    dt = 1./N
    b = np.random.normal(0.,1.,int(N)) * np.sqrt(dt) #Brownian Increments
    W = np.cumsum(b) #Generating Brownian Paths
    return W, b 

# inputs
Bm = Brownian(5, N)[1]    # Brownian increments 
Wm = Brownian(5,N) [0]

t = np.linspace(0.,1.,N)

plt.title('Brownian Motion Increments with N=64 and normalized distribution')
plt.plot(t,Bm)
plt.xlabel('Time')
plt.ylabel('Values')
plt.show()

plt.title('Brownian Motion with N=64 and normalized distribution')
plt.plot(t,Wm)
plt.xlabel('Time')
plt.ylabel('Values')
plt.show()



