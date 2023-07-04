import pandas as pd 
filr=("/home/onedata/Downloads/empy/detailed-03-07-2023-03-07-2023.csv")
data=pd.read_csv(filr)
#aree={"Project Name":"first",'Spent Time':"sum"}
data=data.groupby('User Name')
data=data.first()
print(data.drop_duplicates(                                                                                                                                                                                              ))