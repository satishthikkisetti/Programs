import pandas as pd
data=['steve','35','male','3.5']
series= pd.Series(data)
print(series)

data=['steve','35','male','3.5']
series= pd.Series(data,index=['Name','Age','gender','rating'])
print(series)
