#Binomial Model

import numpy as np
import math

#s : Stock Price
#u : Price of option if it goes up
#d : Price of option if it goes down
#n : Number of coin tosses    

def generate_binomial_pricing_of_stock(s,u,d,n):

	stkval = np.zeros((n + 1, n + 1))
	stkval[0, 0] = s
	for ii in range(1, n+1):
		stkval[ii, 0] = stkval[ii-1, 0] * u
		for jj in range(1, ii+1):
			stkval[ii,jj] = stkval[ii-1, jj-1] * d
	print (stkval)

generate_binomial_pricing_of_stock(100,2,0.5,2)
generate_binomial_pricing_of_stock(100,2,0.5,3)
generate_binomial_pricing_of_stock(100,2,0.5,4)
