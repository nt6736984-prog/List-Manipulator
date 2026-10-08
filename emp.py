# import pandas as pd
# data=pd.read_csv("Messy_Employee_dataset.csv")
# df=pd.DataFrame(data)
# print(df)
# df[['Department','Region']]=df['Department_Region'].str.split('-',expand=True)

# print(df)
# df.info()

# print(df['Department_Region'].str.split('-',expand=True))
import pandas as pd
da=pd.read_csv("data.csv")
df=pd.DataFrame(da)
print(df)
df[['Department','Region']]=df['department_region'].str.split('-',expand=True)
print(df)
print (df.info())