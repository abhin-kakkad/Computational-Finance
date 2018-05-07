import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from random import gauss
from math import exp, sqrt

class parameters():
    #parameters to be used for program

    def __init__(self):
        
        self.S = 50                     #underlying asset price
        self.v = 0.30                  #volatility
        self.r = 0.05                  #10 year risk free rate
        self.T = 365.0/365.0           #years until maturity
        self.K = 50                     #strike price
        self.B = 45                    #barrier price
        self.delta_t = .001            #timestep
        self.N = self.T/self.delta_t   #Number of discrete time points
        self.simulations = 1000        #num of simulations

    def print_parameters(self):
       
        print ("---------------------------------------------")
        print ("Pricing a down and out option")
        print ("---------------------------------------------")
        print ("Parameters of Barrier Option Pricer:")
        print ("---------------------------------------------")
        print ("Underlying Asset Price = ", self.S)
        print ("Volatility = ", self.v)
        print ("Risk-Free 10 Year Treasury Rate =", self.r)
        print ("Years Until Expiration = ", self.T)
        print ("Time-Step = ", self.delta_t)
        print ("Discrete time points =", self.N)
        print ("Number of Simulations = ", self.simulations)
        print ("---------------------------------------------")
    

class down_and_out_mc(parameters):

    def __init__(self):
        
        parameters.__init__(self)
        self.payoffs = []
        self.price_trajectories = []
        self.discount_factor = exp(-self.r * self.T)

    def call_payoff(self,s):
        
        self.cp = max(s - self.K, 0.0)
        return self.cp

    def calculate_payoff_vector(self):

        for i in range(0, self.simulations):
            self.stock_path = []
            self.S_j = self.S
            for j in range(0, int(self.N-1)):
                self.xi = gauss(0,1.0)

                self.S_j *= (exp((self.r-.5*self.v*self.v) * self.delta_t + self.v *sqrt(self.delta_t) * self.xi))

                self.stock_path.append(self.S_j)
            self.price_trajectories.append(self.stock_path)
            if max(self.stock_path) > self.B:
                self.payoffs.append(self.call_payoff(self.stock_path[-1]))
            elif max(self.stock_path) < self.B:
                self.payoffs.append(0)

        return self.payoffs           

    def compute_price(self):
   
        self.np_payoffs = np.array(self.payoffs, dtype=float) 
        self.np_Vi = self.discount_factor*self.np_payoffs 
        self.price = np.average(self.np_Vi)

    def print_price(self):

        print (str("Call Price: %.4f") % self.price)
        print ("---------------------------------------------")

    def plot_trajectories(self):

        print("Creating Plot...")

        self.np_price_trajectories = np.array(self.price_trajectories, dtype=int)
        self.times = np.linspace(0, self.T, self.N-1)
    
        self.fig = plt.figure()
        self.ax1 = plt.subplot2grid((1,1),(0,0))
        for sublist in self.np_price_trajectories:
            if max(sublist) < self.B:
                self.ax1.plot(self.times,sublist,color = 'cyan')
            else:
                self.ax1.plot(self.times,sublist,color = '#e2fb86')
        plt.axhline(y=45,xmin=0,xmax=self.T,linewidth=2, color = 'red', label = 'Barrier')
    
        for label in self.ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
        self.ax1.grid(True)
    
        #plotting
        plt.xticks(np.arange(0, self.T+self.delta_t, .1))
        plt.suptitle('Stock Price Trajectory', fontsize=40)
        plt.legend()
        self.leg = plt.legend(loc= 2)
        self.leg.get_frame().set_alpha(0.4)
        plt.xlabel('Time (in years)', fontsize = 30)
        plt.ylabel('Price', fontsize= 30)
        plt.show()


#Initialize and print parameters
prm = parameters()
prm.print_parameters()

#Price/print the option
ui_mc = down_and_out_mc()
ui_mc.calculate_payoff_vector()
ui_mc.compute_price()
ui_mc.print_price()

#plot
ui_mc.plot_trajectories()