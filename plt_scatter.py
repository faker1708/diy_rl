import matplotlib.pyplot as plt
# import numpy as np
import random


class plt_scatter():

    def __init__(self):


        plt.ion()  # 开启交互模式
        plt.subplots()

        self.plt = plt


    def paint(self):
        plt = self.plt
        plt.clf()     # 清空画布
        plt.xlim(-1, 7)      # 因为清空了画布，所以要重新设置坐标轴的范围
        plt.ylim(-1, 7)


        x = self.x
        y = self.y
        # x = random.randint(0,6)
        # y = random.randint(0,6)

        plt.scatter(x, y)
        plt.pause(0.2)

    def remain(ps):
        ps.plt.ioff()
        ps.plt.show()


ps = plt_scatter()

for j in range(10):

    # ps.x = random.randint(0,6)
    ps.x = 5
    ps.y = random.randint(0,6)

    ps.paint()
ps.remain()




