import pandas as pd
df=pd.read_csv("abhinav.csv")
# these are the basic information of  data that can bring you understanding about the what the database and how many rows and columns are there in it
print(df.head())
#print(df.tail())
#print(df.describe())
#print(df.info())
#print(df.columns)
#print(df.dtypes)
#print(df.shape)
#print(type(df))
df.rename(columns={'Use_Cases':'AI_Use_Cases'},inplace=True)

#print(df.drop_duplicates())


#print(df.fillna(0))
#print(df[df.Student_Name=='Aarav'].head(10))
#print(df.iloc[0:10])


