import numpy as np
import pandas as pd



df= pd.read_csv(r'D:\Project-to-learn\Olympic-Analysis-web-app\Data\athlete_events.csv')
region_df=pd.read_csv(r"D:\Project-to-learn\Olympic-Analysis-web-app\Data\noc_regions.csv")

def preprocessor():
    global df,region_df
    # Filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # Merge with region data
    df = pd.merge(region_df,on='NOC',how='left')
    # Drop unnecessary columns
    df.drop_duplicates(inplace=True)
    # One hot encoding for Medal
    df=pd.concat(df,pd.get_dummies(df['Medal']),axis=1)

    return df