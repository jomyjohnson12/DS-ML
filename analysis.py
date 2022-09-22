import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_excel('price history.xlsx',index_col=None,na_values=['NA'],usecols="B,E")
df = pd.DataFrame(data)
print(df)
x = np.array(df['OPEN']).reshape(-1,1)
y = np.array(df['CLOSE']).reshape(-1,1)
df.dropna (inplace=True)

print(x)
print(y)

plt.plot(x,y)
plt.show()
