import numpy as np
import matplotlib.pyplot as plt


#constants
mu, sigma = .15, .4  
So = 55.25
T = 2.0
N = 64.0 #divisions for the calculation / increment in step size

#Brownian Motion
def Brownian(seed, N):
    
    np.random.seed(seed)
    dt = 1./N
    b = np.random.normal(0.,2.,2*int(N))* np.sqrt(dt)  #Brownian Increments
    W = np.cumsum(b) #Generating Brownian Paths
    return W, b
 
# Exact Solution
def ExactSolution(So, mu, sigma, W, T, N):    
    t = np.linspace(0.,2.,N+1)
    S = []
    S.append(So)
    for i in range(1,int(N+1)):
        drift = (mu - 0.5 * sigma**2) * t[i]
        diffusion = sigma * W[i-1]
        S_temp = So*np.exp(drift + diffusion)
        S.append(S_temp)
    return S, t

W = Brownian(5, N)[0]                           # Brownian increments
ESoln = ExactSolution(So, mu, sigma, W, T, N)    


# Plotting
X = ESoln[0]         # Exact solution
time = ESoln[1]      # Time increments
plt.title('Geometric Brownian Motion with S0=55.25, mu=0.15, sigma=0.4')
plt.xlabel('Time')
plt.ylabel('Values')
plt.plot(time, X, label = 'Geometric Brownian Motion')
plt.show()
