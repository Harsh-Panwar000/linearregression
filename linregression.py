import numpy as np
import matplotlib.pyplot as plt


x_val = input("Enter your x-values separated by commas: ")
x_val = list(map(int, x_val.split(",")))

one_vector = [1] * len(x_val)

data = np.array([x_val,one_vector])
data = data.transpose()

y = input("Enter your y-values separated by commas: ")
y = np.array(list(map(int, y.split(",")))).transpose()

output = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(data),data)),np.transpose(data)),y)
intercept = np.round(output[1])
slope = np.round(output[0])

line = slope*np.array(x_val) + intercept
plt.plot(x_val,y.transpose(),"o")
plt.plot(x_val, line)
plt.show()
