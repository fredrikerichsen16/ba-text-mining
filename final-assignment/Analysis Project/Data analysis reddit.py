from numpy import concatenate
import pandas as pd
data = pd.read_csv('btc_reddit_sentiment_1.csv' , sep=';')
data1 = pd.read_csv('BTC-USD.csv')

#day

data["Date"] = data["date"]

average_sentiment = (data.groupby([data['Date']], as_index=False)["sentiment"].mean())
#print(average_sentiment)

data1["Result"] = (data1["Close"] - data1["Open"])
data1["Percentage_change"] = ((data1["Close"] - data1["Open"]) / data1["Open"]) * 100

start_date = '2021-01-01'
end_date = '2021-08-16'

mask = (data1['Date'] >= start_date) & (data1['Date'] <= end_date)
all_the_dates = data1.loc[mask]
all_the_dates1 = all_the_dates[["Date", "Result"]]
all_the_dates2 = all_the_dates[["Date", "Percentage_change"]]
#print(all_the_dates1)

concatenated = all_the_dates1.merge(average_sentiment, on='Date', how='left')
#print(concatenated)

#week

data['Date'] = pd.to_datetime(data['Date'])

week = data.groupby(pd.Grouper(key="Date", freq="1W")).mean()
week1 = week[["sentiment"]]
#print(week1)

all_the_dates1['Date'] = pd.to_datetime(all_the_dates1['Date'])

allth = all_the_dates1.groupby(pd.Grouper(key="Date", freq="1W")).mean()
#print(allth)

concatenated1 = allth.merge(week1, on='Date', how='left')
#print(concatenated1)

#month
data['Date'] = pd.to_datetime(data['Date'])

month = data.groupby(pd.Grouper(key="Date", freq="1M")).mean()
month1 = month[["sentiment"]]
#print(month1)

all_the_dates2['Date'] = pd.to_datetime(all_the_dates2['Date'])

allth3 = all_the_dates2.groupby(pd.Grouper(key="Date", freq="1M")).mean()
#print(allth3)

concatenated3 = allth3.merge(month1, on='Date', how='left')
#print(concatenated3)


#Jochem can you try different kinds of data analysis and then create diagrams that we can put in the report (don't save the images, just keep the jupyter notebook ready, cause we're gonna use different data once it's available).
#Different kinds like: between weekly sentiment and weekly percent change in price, between daily sentiment and daily percent change in price, and daily/weekly sentiment and whether it goes up or down in the next day/week (and maybe more stuff you can think of, like predicting sudden price movements or something)