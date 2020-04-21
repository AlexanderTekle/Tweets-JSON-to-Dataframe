import jsonlines
import os
import pandas as pd


count=0;
df_tweets = pd.DataFrame({'tweet': []})

for filename in os.listdir('./json'):
    with jsonlines.open("./json/" + filename) as f:
        for obj in f:
            df_tweets.loc[count]=str(obj['full_text']);
            print(filename + ": " + str(count) + ". " + obj['full_text']);
            count=count+1;

df_tweets.to_pickle("./tweets.pkl")
print(df_tweets.head())
