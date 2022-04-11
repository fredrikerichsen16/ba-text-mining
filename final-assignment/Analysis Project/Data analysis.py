from numpy import concatenate
import pandas as pd
data = pd.read_csv('btc_sentiment_1.csv' , sep=';')
data1 = pd.read_csv('BTC-USD.csv')

data1["Result"] = (data1["Close"] - data1["Open"])

filter_list = ['2022-01-19', '2022-01-20', '2022-02-09', '2022-02-14', '2022-02-15', '2022-02-16', '2022-02-17', '2022-02-18']
all_the_dates = (data1[data1['Date'].isin(filter_list)])
all_the_dates1 = all_the_dates[["Date", "Result"]]
print(all_the_dates1)

data['date'] = data['date'].astype(str)
data['actual_date'] = data['date'].str[0:10]
data['time'] = data['date'].str[12:]

#print(data["sentiment"].value_counts())
#total 19989
#0 10138
#1 6742
#-1 3109

#print(data["actual_date"].value_counts())
average_sentiment = (data.groupby([data['actual_date']])["sentiment"].mean())
print(average_sentiment)

concatenated = pd.concat([all_the_dates1, average_sentiment], axis=1, ignore_index=False)
#concatenated1 = concatenated.dropna(axis=0) 
#print(concatenated)

#There's a file in the drive called BTC-USD.csv
#First you can graph the average daily sentiment against the daily price to see what it looks like
#Then calculate the correlation coefficient, but it'll probably be low so it's probably better to see if you can predict whether the bitcoin price goes up or down in a day based on the sentiment the day before (maybe - I think so cause I saw somebody else doing that)