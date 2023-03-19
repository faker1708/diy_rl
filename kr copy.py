


'''
业务需求，已知一个简单的游戏与简单的强化学习算法，请实现它

多臂老虎机
每个老虎机的输出是一个正态分布，未知其均值与标准差。

目标，找出均值最大的那个老虎机

算法：
    初始价值设置为很大，然后每次以 p 的概率访问价值最大的某个老虎机，以 1-p的概率随机访问一个老虎机

    价值更新，每次计算出累积 的均值。均值作为价值。


    流式平均，平均函数 的递推形式
    v[n] =  (   (n-1)*v [n-1] + a[n] ) / n




'''

import random
import torch


class lhj ():

    def __init__(self,index) -> None:
        self.index = index  # 记录它的编号
        means = random.randint(2**9,2**10-1)
        self.means = means
        

        # 初始化游戏过程
        self.value= 999
        self.time = 1
        

    def update_value(self,new_money):
        old_v =self.value
        new_v =( old_v * self.time + new_money ) / (self.time+1)
        
        
        self.value= new_v
        self.time+=1


    def pop(self):
        means = self.means
        std = 30
        new_money = torch.normal(means,std,(1,1))
        
        self.update_value(new_money)
        # return x

class two_arm():

    # def update(lhj_x,new_money,time):

    def get_max_lhj(self):
        jl = self.jl
        max_one = jl[0]
        for i,lhj_x in enumerate(jl):
            if(lhj_x.value>max_one.value):
                # max_v =lhj_x.value
                max_one = lhj_x
        return max_one

    
    def main(self):
        
        k = 2 # 老虎机的个数

        jl = list()

        for i in range(k):

            lhj_x = lhj(i)

            jl.append(lhj_x)
            print(lhj_x.means)
        print('\n\n')
        self.jl = jl

        op = 0
        p = 0.9 # 这个概率访问最大价值的老虎机，1-p 的概率临幸其它老虎机

        pc = 2**10
        pp = pc * p

        # 开始训练
        tc = 303
        for epoch in range(tc):

            ch = random.randint(0,pc-1)
            if(ch<pp):
                # 随机值比阈值大
                # 中p
                op = 1
            else:
                # 未中P
                op = 0
            
            # mo = jl[0]
            # if(op == 1):
                # 选择价值最大老虎机


            mo = self.get_max_lhj()
            # else:
            if(op == 0):
                # 如果 需要变异，则另取一个机器
                max_i = mo.index
                random_index = random.randint(0,k-2)
                if(random_index>= max_i):
                    random_index+=1
                mo = jl[random_index]


            
            mo.pop()
            print(mo.index,float(mo.value))




a = two_arm()
a.main()
