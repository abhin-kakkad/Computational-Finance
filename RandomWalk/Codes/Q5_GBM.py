import numpy as np
import matplotlib.pyplot as plt

#constants
mu, sigma = .18, .3  
So = 100
T = 1.0
N = 240.0 #divisions for the calculation / increment in step size

#Brownian Motion
def Brownian(seed, N):
    
    np.random.seed(seed)
    dt = 1./N
    b = np.random.normal(0.,1.,int(N)) * np.sqrt(dt) #Brownian Increments
    W = np.cumsum(b) #Generating Brownian Paths
    return W, b 

# Euler Approximation for Geometric Brownian Motion
def GBM(So, mu, sigma, b, T, N, M):
    dt = M * (1/N)  # EM step size
    L = N / M
    wi = [So]
    for i in range(0,int(L)):
        Winc = np.sum(b[(M*(i-1)+M):(M*i + M)])
        w_i_new = wi[i]+mu*wi[i]*dt+sigma*wi[i]*Winc
        wi.append(w_i_new)
    return wi, dt

# inputs
b = Brownian(15, N)[1]    # Brownian increments 
M = 2                    
L = N/M

GBM_approx = GBM(So, mu, sigma, b, T, N, M)[0]

print(GBM_approx)


