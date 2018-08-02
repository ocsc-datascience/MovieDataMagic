#!/usr/bin/env python3
import sys
import pandas as pd


# data with twitter hashtags
fname_twitter = "../data/all_movies_with_twitter.csv"
fname_ratings = "../data/all_movies_with_ratings.csv"

df_t = pd.read_csv(fname_twitter)
df_r = pd.read_csv(fname_ratings)



df_combined = pd.merge(df_t,df_r[ ['movie_title','RT_title',
                                   'critics_rating','audience_rating'] ],
                                  on=['movie_title'],how='left')



del df_combined['row']
df_combined.reset_index(drop=False,inplace=True)
df_combined.rename(columns={'index':'row'},inplace=True)

df_combined.to_csv('../data/all_movies_with_twitter_and_ratings.csv')
