import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# dataset = pd.read_csv('C:\\Users\\manik\\Downloads\\hashin55\\hashin55\\TestData.csv')
# x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
# y = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
# x, y = np.array(x), np.array(y)
# x_train, x_test, y_train, y_test = train_test_split(x, y)
# lr = LinearRegression()
# lr.fit(x_train, y_train)
# y_pred = lr.predict(x_test)
# print(x_train)
# print("-------")
# print(x_test)


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 14, 26, 21, 15, 23, 26, 11]
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)
x_train, x_test, y_train, y_test = train_test_split(x, y)

lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

x_test [9, 10]
x_test = np.array(x_test).reshape(-1, 1)
y_pred = lr.predict(x_test)
print(y_pred)
print("-------")
print(x_test)

plt.plot(x_train, y_train, color = "red")
plt.plot(x_test, lr.predict(x_test), color = "green")
plt.title("Salary vs Experience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()