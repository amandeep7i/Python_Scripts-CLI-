import pandas as pd

# TO get the csv file into dataframes

df = pd.read_csv('data.csv')

# To remove NULL values from the csv file
df= df.dropna()
# calculate total impressions for the age group 30-34
dfn = df.query('age =="30-34"')
print((dfn.groupby(['age'])).impressions.sum())
print('===========================')

#  get all ad_ids for every campaign_id (a campaign contains multiple ads)
print('Campaign wise ad count')
print((df.groupby(['campaign_id'])).ad_id.count())
print('===========================')

# get total clicks where report_start between dates 19/08/2017 to 22/08/2017 (both inclusive)
dfr = df.query('reporting_start>="17/08/2017" and reporting_end<="22/08/2017"')
print("Total clicks in the referred starting and ending date ",end=":  ")
print(dfr.clicks.sum())
print('===========================')