#Delta-Hedging with variable Rate of Interest

#s : Stock Price
#u : Fraction of increase in price if it goes up
#d : Fraction of increase in price if it goes down
#n : Number of coin tosses  
#K : Strike Price
#S0 : Initial Stock Price

def delta_hedging_constant(S0,u,d,length,r,k):
	length = length+1
	arr = [[0]*(length+1)]*(length+1)
	for i in range(0,length+1):
		arr[i] = [0]*(length+1)
	arr[0][1] = u*S0
	for i in range(1,length+1):
		arr[i][1] = d*arr[i-1][1]
		for j in range(2,i+1):
			arr[i][j] = (arr[i-1][j-1]*u)
	s = [[0]*(length+1)]*(length+1)
	for i in range(0,length+1):
		s[i] = [0]*(length+1)
	s[1][1] = S0
	for i in range(2,length+1):
		s[i][1] = s[i-1][1]*d
		if i==length:
			if s[i][1]>k:
				s[i][1] = k
			else:
				s[i][1] = 0
		for j in range(2,i+1):
			s[i][j] = s[i-1][j-1]*u
			if i==length:
				if s[i][j] > k:
					s[i][j] = s[i][j]-k
				else:
					s[i][j] = 0
	optval = [[0]*(length+1)]*(length+1)

	for i in range(0,length+1):
		optval[i] = [0]*(length+1)
	for i in range(0,length+1):
		optval[length][i] = s[length][i]
	for i in range(length-1,0,-1):
		r = 1.0/float(i)
		p = (1+r-d)/(u-d)
		q = (u-1-r)/(u-d)
		for j in range(1,i+1):
			optval[i][j] = (q*optval[i+1][j] + p*optval[i+1][j+1])/(1+r)

	print ("The value of k is:", length-1)			
	print("Option price is", optval[1][1])

delta_hedging_constant(4.0,2.0,1/2,2,1/4.0,4.0)
