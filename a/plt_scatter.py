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
        plt.xlim(0-1, self.width+1)      # 因为清空了画布，所以要重新设置坐标轴的范围
        plt.ylim(0-1, self.hight+1)


        x = self.x
        y = self.y
        # x = random.randint(0,6)
        # y = random.randint(0,6)



        plt.scatter(x, y,c= 'blue')
        
        x = self.tx
        y = self.ty
        
        plt.scatter(x, y,c= 'deeppink')
        plt.pause(0.5)

    def remain(ps):
        ps.plt.ioff()
        ps.plt.show()

# 样例
# ps = plt_scatter()

# for j in range(10):

#     # ps.x = random.randint(0,6)
#     ps.x = 5
#     ps.y = random.randint(0,6)

#     ps.paint()
# ps.remain()




