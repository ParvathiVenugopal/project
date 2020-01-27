import pandas as pd
data=pd.read_csv("info.csv")
df=pd.DataFrame(data)
print(df)
print(data.head(n=3))
print(data.tail(n=3))