import pandas as pd
data={
    'Name':['steve','lia','vin','katie'],
    'Age':[32,28,45,38],
    'Gender':['Male','Female','Male','Female'],
    'Rating':[3.45,4.6,3.9,2.78]
}
print(data)
df=pd.DataFrame(data,index=['a','b','c','d'])
print(df)
print(df.describe())


s=pd.Series([10,20,30,40],index=['a','b','c','d'])
print("Series:\n",s)
print("Values",s.values)
print("Index",s.index)
print("Access element",s['b'])