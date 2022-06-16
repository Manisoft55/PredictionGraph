

from operator import mod
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
y = [11, 65, 90, 94, 77, 12, 97, 79]
x, y = np.array(x), np.array(y).reshape(-1, 1)

model = LinearRegression().fit(y, x)
r_sq = model.score(y, x)
# print('coefficient of determination:', r_sq)
# coefficient of determination: 0.8615939258756776
# print('intercept:', model.intercept_)
# intercept: 5.52257927519819
# print('slope:', model.coef_)
# slope: [0.44706965 0.25502548
y_pred = model.predict(y)
# print('predicted response:', y_pred, sep='\n')

y_new = [80, 86, 72]
y_new = np.array(y_new).reshape(-1, 1)
y_new_pred = model.predict(y_new)
x_new = [2018, 2019, 2020]
print(y_pred)
print("---------------")
print(y_new_pred)

plt.plot(x, y_pred, color = "red")
plt.plot(x_new, model.predict(y_new), color = "green")
plt.title("Predict Average Yield and Price")
plt.xlabel("Years")
plt.ylabel("Average yield and price")
plt.show()

