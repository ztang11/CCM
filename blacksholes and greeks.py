#Pricing engine module that calculates Option prices and Greeks with black scholes
#The Black Scholes Formula
""" 
# CallPutFlag - This is set to 'c' for call option, anything else for put
# S - Stock price
# K - Strike price
# T - Time to maturity
# r - Riskfree interest rate
# d - Dividend yield
# v - Volatility
"""
from scipy.stats import norm
from math import *
def BlackScholes(CallPutFlag,S,K,T,r,d,v):
  d1 = (log(float(S)/K)+((r-d)+v*v/2.)*T)/(v*sqrt(T))
  d2 = d1-v*sqrt(T)
  if CallPutFlag=='c':
    return S*exp(-d*T)*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)
  else:
    return K*exp(-r*T)*norm.cdf(-d2)-S*exp(-d*T)*norm.cdf(-d1)


  #Greeks in the Blacksholes
  #Calculating the partial derivatives for a Black Scholes Option (Call)
  
"""
Return:
Delta: partial wrt S
Gamma: second partial wrt S
Theta: partial wrt T
Vega: partial wrt v
Rho: partial wrt r 
"""
from scipy.stats import norm
from math import *
def Black_Scholes_Greeks_Call(S, K, r, v, T, d):
  T_sqrt = sqrt(T)
  Delta_Call = norm.cdf(d1)
  Gamma_Call = norm.pdf(d1)/(S*v*T_sqrt)
  Theta_Call =- (S*v*norm.pdf(d1))/(2*T_sqrt) - r*K*exp( -r*T)*norm.cdf(d2)
  Vega_Call = S * T_sqrt*norm.pdf(d1)
  Rho_Call = K*T*exp(-r*T)*norm.cdf(d2)
    return Delta_Call, Gamma_Call, Theta_Call, Vega_Call, Rho_Call

#Calculating the partial derivatives for a Black Scholes Option (Put)

def Black_Scholes_Greeks_Put(S, K, r, v, T, d):
  T_sqrt = sqrt(T)
  Delta_Put = -norm.cdf(-d1)
  Gamma_Put = norm.pdf(d1)/(S*v*T_sqrt)
  Theta_Put = -(S*v*norm.pdf(d1)) / (2*T_sqrt)+ r*K * exp(-r*T) * norm.cdf(-d2)
  Vega_Put = S * T_sqrt * norm.pdf(d1)
  Rho_Put = -K*T*exp(-r*T) * norm.cdf(-d2)
    return Delta_Put, Gamma_Put, Theta_Put, Vega_Put, Rho_Put
