import numpy as np

'''
Function to Calculate the Price of American Options
Inputs- strikePrice- Strike Price
        Smax- spot price
        time- Maturity (in years)
        sigma- volatility 
        rate- risk free interest rate
        timeSteps - number of time steps
        priceSteps- number of price steps
        
'''

def OptioncallI(Smax,priceSteps,time,timeSteps,strikePrice,rate,sigma):
    
    
    ds=Smax/float(priceSteps)   
    dt=time/float(timeSteps)      
    
    i=np.arange(1,priceSteps,dtype=np.float)
    
    a=0.5*dt*(rate*i-sigma**2*i**2)
    b=1+ dt*(sigma**2*i**2+rate)
    c=-0.5*dt*(sigma**2*i**2+rate*i)
    
    A=np.diag(b)+np.diag(a[1:],k=-1)+np.diag(c[0:priceSteps-2],k=1)

    F=np.zeros((timeSteps+1,priceSteps+1))  
    
#Boundary Condition
    
    F[timeSteps,:]=np.maximum(strikePrice-np.arange(0,Smax+ds/2.0,ds,dtype=np.float),0)
    F[:,0]=strikePrice
    F[:,priceSteps]=0
    
    for j in range(timeSteps-1,-1,-1):
        d=F[j+1,1:priceSteps] 
        d[0]=d[0]-a[0]*F[j,0]   
        d[priceSteps-2]=d[priceSteps-2]-c[priceSteps-2]*F[j,priceSteps]  

        F[j,1:priceSteps]=np.linalg.solve(A,d) 
        F[j,:]=np.maximum(strikePrice-np.arange(0,Smax+ds/2.0,ds,dtype=np.float),F[j,:]) 
    return F[0,int((priceSteps+1)/2)] 

print ("The value of an American put option is" , OptioncallI(100,20,5/12.0,10,50,0.1,0.4))

