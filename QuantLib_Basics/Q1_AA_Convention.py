import QuantLib as ql

date = ql.Date(17,4,2018) 
print (date)

annual_rate = 0.10
days = ql.ActualActual()
int_type = ql.Compounded
time = ql.Semiannual

interest = ql.InterestRate(annual_rate,days,int_type,time)
print(interest)

x = interest.compoundFactor(5)
y =  interest.discountFactor(5)

print(x,y)