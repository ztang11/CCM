import datetime
from random import gauss
from math import exp, sqrt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
"""
# S - stock price
# v - volatility
# r - riskfree interest rate
# T - Time to maturity
"""


def generate_asset_price(S,v,r,T):
    return S * exp((r - 0.5 * v**2) * T + v * sqrt(T) * gauss(0,1.0))

""""
getting the array of the price we generate 
"""


def simulation_array(k):
    for i in range(0, simulations):
        for j in range(0, T1):
            S_T = generate_asset_price(S, v, r, T)
            k[i, j] = (S_T)
    return k

"""
plotting the simulation array that we got
"""

def simu_plot(k):
    plt.figure(1)
    sns.kdeplot(k[:, -1])

    plt.figure(2)
    for i in k:
        plt.plot(i)
    return
"""
define monte carlo simulation
"""


def main():
    global T1, S, v, r, T, simulations
    S = 57.30 # underlying price
    v = 0.20 # vol of 20%
    r = 0.0015 # rate of 0.15%

    T1 = (datetime.date(2014,9,30) - datetime.date(2014,9,1)).days
    T = T1/ 365.0

    simulations = 10000
    k=np.zeros(shape=(simulations,T1))

    k=simulation_array(k)

    simu_plot(k)
    plt.show()

    return

if __name__ == "__main__":
    main()
    
