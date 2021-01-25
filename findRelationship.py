# Calculate r squared to find best relationships
# possibly lambda function?
# import the dataframe from createDF.py
# need to make a date string to get the days dataframe

import pandas as pd
import numpy as np
from datetime import datetime
import scipy.stats

startTime = datetime.now()

# get the days date
dateString = datetime.strftime(datetime.now(), '%Y_%m_%d')

# declare the path, this method of the variable and raw string makes the code
# a bit more readable
dataPath = (r'C:\Users\Vincent\Documents\GitHub'
            r'\Basketball-Analysis\Excel Sheets'
            r'\Team Stats ' + dateString + '.csv')

# get the data
league_data_df = pd.read_csv(dataPath)

# I think I want to drop 'string' formatted data to make it easier to 
# complete the necessary math, but we can worry about that later, see how it
# goes

# scipy.stats.linregress(df1[['bins', 'one']].to_numpy()).rvalue ** 2
# above is example code from SO

decimals = 2
print(round((scipy.stats.linregress
       (league_data_df[['W', 'points']].to_numpy()).rvalue ** 2),2))

print(datetime.now()-startTime)