import numpy as np
import matplotlib.pyplot as plt


#constants
mu, sigma = .00081, .018  
So = 636.99
T = 2.0
N = 252.0 #divisions for the calculation / increment in step size

#Brownian Motion
def Brownian(seed, N):
    
    np.random.seed(seed)
    dt = 1./N
    b = np.random.normal(0.,1.,int(N))  #Brownian Increments
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
plt.plot(time, X, label = 'Seed=5')


W = Brownian(15, N)[0]                           # Brownian increments
ESoln = ExactSolution(So, mu, sigma, W, T, N)    

# Plotting
X = ESoln[0]         # Exact solution
time = ESoln[1]      # Time increments
plt.plot(time, X, label = 'Seed=15')


W = Brownian(22, N)[0]                           # Brownian increments
ESoln = ExactSolution(So, mu, sigma, W, T, N)    

# Plotting
X = ESoln[0]         # Exact solution
time = ESoln[1]      # Time increments
plt.plot(time, X, label = 'Seed=22')

plt.title('GBM for Amazon')
plt.xlabel('Time')
plt.ylabel('Values')

n=253
I=np.zeros([n])
file = open('data.txt', 'r+')

for i in range(0,n):
    I[i]= file.readline()

file.close() 

plt.plot(time,I, label="Actual Data")
plt.legend(loc='upper left')
plt.show()
