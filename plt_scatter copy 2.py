import matplotlib.pyplot as plt
import numpy as np


class plt_scatter():

    def __init__(self):
        


    def paint(self):


def change(arr):
    x = []
    y = []
    for i in range(len(arr)):
        x.append(arr[0])
        y.append(arr[1])
    x = np.array(x)
    y = np.array(y)
    return x, y


plt.ion()  # 开启交互模式
plt.subplots()

arr = [0,0]
arr = np.array(arr)
for j in range(10):
    plt.clf()     # 清空画布
    plt.xlim(-1, 7)      # 因为清空了画布，所以要重新设置坐标轴的范围
    plt.ylim(-1, 7)



    # for i in range(6):
    arr[0] = np.random.randint(0,6,1)
    arr[1] = np.random.randint(0,6,1)
    x, y = change(arr)
    plt.scatter(x, y)
    plt.pause(0.2)


plt.ioff()
plt.show()