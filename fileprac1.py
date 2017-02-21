import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import quandl as qn

def get_data(list):
    mydata = qn.get(list[1], start_date=list[2], end_date=list[3],
                       transformation='diff')  # gives you pandas dataframe directly
    return mydata

def dis_plot(df,nm,i):
    plt.figure(i)
    sns.kdeplot(np.log(df.Settle + 1 + np.max(np.abs(df.Settle))))
    plt.title(nm)
    return 
# plot the figure

def main():
    dict1 = {0:['Crude Oil', 'CHRIS/CME_CL2.6' , '2017-01-03', '2017-02-03'],1:['Soybeans', 'CHRIS/CME_S2.6', '2017-01-03', '2017-02-03'],\
             2:['Gold', 'CHRIS/CME_GC2.6', '2017-01-03', '2017-02-03']}
    
    # extract data on crude oil, soybeans and gold

    for i in range (0,len(dict1)):
        df = get_data(dict1[i])
        dis_plot(df,dict1[i][0],i)

    plt.show()
# create a loop to get the data and plot figure for three times
    return

if __name__ == "__main__":
    main()
# calling the function 
