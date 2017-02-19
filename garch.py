'''Initial code for the garch model. I still need to use functions and incorporate a way to solve for gamma, alpha and beta. '''

from pymongo import MongoClient
import pandas as pd
import numpy as np
import math

connection = MongoClient()

db = connection.ccm

data = list(db.monte_carlo.find({}, {'_id': 0, 'Future': 1, 'AtM': 1, 'Date': 1}).sort('Date'))

df = pd.DataFrame(data, columns=['Date', 'Future', 'AtM', 'Log_Returns', 'AtM_Var', 'Norm_AtM_Vol', \
                                 'Stocastic_Factor', 'Simulated_Var', 'Simulated_AtMVol', 'Simulated_Futures', \
                                 'Simulated_Log_returns', 'Error', 'Abs_Error', 'Vol_Error', 'Abs_Vol_Error'])

df.set_index('Date', inplace=True)

df = df.loc['2009-06-15':'2014-12-31']

df['Log_Returns'] = df.Future.pct_change()

df['AtM_Var'] = df['AtM']**2

df['Norm_AtM_Vol'] = df.AtM.divide(math.sqrt(252))

log_mean = df['Log_Returns'].mean()
norm_AtMVol = df['Norm_AtM_Vol'].mean()

df['Stocastic_Factor'] = (df['Log_Returns'] - log_mean).divide(df['Norm_AtM_Vol'])

df['Simulated_Var'][1] = df['AtM_Var'][1]

df['Simulated_Futures'][1] = df['Future'][1]

df['Simulated_Log_returns'][1] = df['Log_Returns'][1]

df['Simulated_AtMVol'][1] = df['Simulated_Var'][1] ** .5

#values of gamma, alpha, beta taken from prototype
gamma = 0.0003343
alpha = 0.0072841
beta = 0.9927159

for i in range(2,len(df.index)):
    df['Simulated_Var'][i] = i

    df['Simulated_Var'][i] = gamma + alpha * (df['Simulated_Log_returns'][i-1] - log_mean)**2 + (beta * df['Simulated_Var'][i-1])

    df['Simulated_AtMVol'][i] = df['Simulated_Var'][i] ** .5

    df['Simulated_Futures'][i] = df['Simulated_Futures'][i-1] * np.exp(log_mean + \
                            (df['Stocastic_Factor'][i] * df['Simulated_AtMVol'][i] / 16))

    df['Simulated_Log_returns'][i] = math.log(df['Simulated_Futures'][i] / df['Simulated_Futures'][i-1])

df['Error'] = df['Log_Returns'] - df['Simulated_Log_returns']

df['Vol_Error'] = df['AtM'] - df['Simulated_AtMVol']

df['Abs_Error'] = df['Error'].abs()

df['Abs_Vol_Error'] = df['Vol_Error'].abs()
print (df['Abs_Error'])
