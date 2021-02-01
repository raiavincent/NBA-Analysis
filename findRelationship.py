# Calculate r squared to find best relationships
# possibly lambda function?
# DONE: import the dataframe from createDF.py
# DONE: need to make a date string to get the days dataframe
# do I have to make a whole ass dataframe then do the math?

import pandas as pd
from datetime import datetime
import scipy.stats
from variable import r2

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

league_data_df = league_data_df[r2]

# I think I want to drop 'string' formatted data to make it easier to 
# complete the necessary math, but we can worry about that later, see how it
# goes

# scipy.stats.linregress(df1[['bins', 'one']].to_numpy()).rvalue ** 2
# above is example code from SO

decimals = 2
print(round((scipy.stats.linregress
       (league_data_df[['W', 'points']].to_numpy()).rvalue ** 2),decimals))


# https://stackoverflow.com/questions/34896455/how-to-do-pearson-correlation
# -of-selected-columns-of-a-pandas-data-frame
# should be able to use the same thing for r2

# realCorr = (league_numbers_df[league_numbers_df.columns[0:]].apply
#             (lambda x: x.corr(league_numbers_df['W'])))
# realCorr = (realCorr.sort_values(ascending=False))

# series = pd.Series(data=league_data_df)

# https://stackoverflow.com/questions/60124004/creating-dataframe-on-the-basis-of-r-squared-value

# df2 = pd.DataFrame({
#     'columns': df1.columns[1:],
#     'r-square_with_bins': [
#         scipy.stats.linregress(df1[['bins', col]].to_numpy()).rvalue ** 2
#         for col in df1.columns[1:]
#     ]
# })

r2_df_dict = {}

for col in league_data_df.columns[3:]:
    r2 = round((scipy.stats.linregress(league_data_df[['W', col]].to_numpy()).rvalue ** 2),decimals)
    print(col + ' ' + ' ' + str(r2))
    if col not in r2_df_dict.keys():
        r2_df_dict[col] = r2

r2_df = pd.DataFrame()
r2_df = r2_df.append(r2_df_dict, ignore_index=True)
r2_df = r2_df.transpose()
r2_df = r2_df.rename(columns={0:'W'})
r2_df =r2_df.sort_values('W',ascending=False)

# r2_df = pd.DataFrame({
#     'columns': league_data_df.columns[4:],
#     'r-square_with_W': [
#         scipy.stats.linregress(league_data_df[['W', col]].to_numpy()).rvalue ** 2
#         for col in league_data_df.columns[1:]
#     ]
# })

print(datetime.now()-startTime)