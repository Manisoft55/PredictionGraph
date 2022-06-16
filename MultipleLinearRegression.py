

from operator import mod
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
# print('coefficient of determination:', r_sq)
# coefficient of determination: 0.8615939258756776
# print('intercept:', model.intercept_)
# intercept: 5.52257927519819
# print('slope:', model.coef_)
# slope: [0.44706965 0.25502548
y_pred = model.predict(x)
# print('predicted response:', y_pred, sep='\n')

x_new = [[63, 32], [58, 29], [55, 31]]
y_new = model.predict(x_new)
print(x_new)
print(y_new)

plt.plot(x, y_pred, color = "red")
plt.plot(x_new, model.predict(x_new), color = "green")
plt.title("Predict Average Yield and Price")
plt.xlabel("Average yield and price")
plt.ylabel("Salary")
plt.show()

