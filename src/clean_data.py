import pandas as pd

def clean_data(df):
    #drop duplicates
    df = df.drop_duplicates()

    #remove missing stars/forks
    df = df.dropna(subset=["stars", "forks"])

    #fill missing language
    df["language"] = df["language"].fillna("Unknown")

    return df