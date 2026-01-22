import pandas as pd
# Importing data set
df = pd.read_excel("/Users/khodeclan/Desktop/sds_datathon_gradsingapore.xlsx")
#CHeck dataset
df = df.copy()
print(df.head())
print(df.shape)
df.info()
df.describe()
#Create new column time taken to find time taken in seconds
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
df.isna().sum()
df["time_taken"] = ""
import numpy as np
df["time_taken"] = np.nan

import pandas as pd
df["date_submitted"] = pd.to_datetime(df["date_submitted"], errors="coerce")
df["time_started"] = pd.to_datetime(df["time_started"], errors="coerce")
df["time_taken"] = df["date_submitted"] - df["time_started"]
df["time_taken_seconds"] = df["time_taken"].dt.total_seconds()
# Drop Unrealistic Values
df_cleaned = df[df["time_taken_seconds"] >= 45].copy()

df_cleaned.to_excel("cleaned_dataset.xlsx", index=False)
df_cleaned.to_excel("/Users/khodeclan/Desktop/cleaned_dataset.xlsx", index=False)

