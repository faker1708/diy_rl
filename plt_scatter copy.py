import matplotlib.pyplot as plt
import numpy as np

def change(arr):
    x = []
    y = []
    for i in range(len(arr)):
        x.append(arr[i][0])
        y.append(arr[i][1])
    x = np.array(x)
    y = np.array(y)
    return x, y


plt.ion()  # 开启交互模式
plt.subplots()
plt.xlim(-1, 7)
plt.ylim(-1, 7)

arr = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
arr = np.array(arr)
x, y = change(arr)
ax = plt.scatter(x, y)
for j in range(100):
    plt.clf()     # 清空画布
    plt.xlim(-1, 7)      # 因为清空了画布，所以要重新设置坐标轴的范围
    plt.ylim(-1, 7)
    for i in range(6):
        arr[i][0] = np.random.randint(0,6,1)
        arr[i][1] = np.random.randint(0,6,1)
    x, y = change(arr)
    plt.scatter(x, y)
    plt.pause(0.2)
plt.ioff()
plt.show()