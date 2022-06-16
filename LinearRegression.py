import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd


x = np.array([2010, 2011, 2012, 2013, 2014, 2015]).reshape((-1, 1))
y = np.array([350, 800, 475, 1340, 700, 1321])
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
y_pred = model.predict(x)

x_new = np.array([2015, 2016, 2017, 2018]).reshape((-1, 1))
y_new = model.predict(x_new)

plt.plot(x, y, color = "red")
plt.plot(x_new, y_new, color = "green")
plt.title("Predict Average Yield and Price")
plt.xlabel("Years")
plt.ylabel("Average yield and price")

fig, ax =plt.subplots(1,1)
data=y_new
column_labels=["Predicted Average value"]
df=pd.DataFrame(data,columns=column_labels)
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values,colLabels=df.columns,rowLabels=["2015","2016","2017","2018"],loc="center")

plt.show()