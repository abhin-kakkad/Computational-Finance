import QuantLib as ql
import matplotlib.pyplot as plt

m_date = ql.Date(21, 7, 2020)
S0 = 100
k = 80
volatality = 0.25
option_type = ql.Option.Call
day_count = ql.Actual365Fixed()
cal = ql.UnitedStates()
r = 0.1
div_rate = 0.0
calc_date = ql.Date(10, 4, 2018)

ql.Settings.instance().evaluationDate = calc_date
payoff = ql.PlainVanillaPayoff(option_type, S0)
exercise = ql.EuropeanExercise(m_date)
european_option = ql.VanillaOption(payoff, exercise)

spot_handle = ql.QuoteHandle(
    ql.SimpleQuote(S0)
)

flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calc_date, r, day_count)
)

dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calc_date, div_rate, day_count)
)

flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calc_date, cal, volatality, day_count)
)

bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_price = european_option.NPV()

print("The theoretical price is ", bs_price)

def binomial_price(bsm_process, steps):
    binomial_engine = ql.BinomialVanillaEngine(bsm_process, "crr", steps)
    european_option.setPricingEngine(binomial_engine)
    return european_option.NPV()

steps = range(2, 100, 1)
prices = [binomial_price(bsm_process, step) for step in steps]
plt.plot(steps, prices, label="Binomial Tree Pricing", lw=2, alpha=0.6)
plt.plot([0,100],[bs_price, bs_price], "r--", label="BSM Pricing", lw=2, alpha=0.6)
plt.xlabel("No. of Steps")
plt.ylabel("Price of Option")
plt.title("Binomial Tree Pricing for Varying Steps")
plt.legend()
plt.show()