


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
import matplotlib.pyplot as plt

class lhj ():

    def __init__(self,index) -> None:
        self.index = index  # 记录它的编号
        means = random.randint(2**9,2**10-1)
        self.means = means
        

        # 初始化游戏过程
        self.value= 1100
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
    

    def get_max_means(self):
        jl = self.jl
        max_one = jl[0]
        for i,lhj_x in enumerate(jl):
            if(lhj_x.means>max_one.means):
                max_one = lhj_x
        return max_one
    
    
    def get_max_time(self):
        jl = self.jl
        max_one = jl[0]
        for i,lhj_x in enumerate(jl):
            if(lhj_x.time>max_one.time):
                max_one = lhj_x
        return max_one
    
    def validate(self):
        mm = self.get_max_means()
        mt = self.get_max_time()
        # print(mt.time)
        
        out = 0
        mmi = mm.index
        mti = mt.index
        if(mmi == mti ):
            # print('成功收敛到正确的值')
            out = 1
        else:
            out = 0
            # print('算法未成功')
        
        va = out
        vv = [va,mmi,mti]
        return vv

    
    def main(self):

        show_pic = 1
        show_pross = 0 # 展示收敛过程
        
        p = 1-2**-3 # 这个概率访问最大价值的老虎机，1-p 的概率临幸其它老虎机
        
        k = 2**5 # 老虎机的个数

        print('保守概率',p)


        tc = 2**17   # 总练习时长

        pass_ratio = 0.5    # 当某个选择投票率到达多少时停止练习
        # pass_ratio = 0.2    # 当某个选择投票率到达多少时停止练习

        
        if(show_pic):
            plt.ion()
            plt.figure(1)


        jl = list()

        for i in range(k):

            lhj_x = lhj(i)

            jl.append(lhj_x)
        #     print(lhj_x.means)
        # print('\n\n')
        self.jl = jl

        op = 0

        pc = 2**14
        pp = pc * p

        # 开始训练
        

        sh_p = 0    # 多久收敛？


        va_list = list()
        x_index = list()
        va=0
        failed = 0
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
                # 如果 需要变异，则随机取一个机器
                # max_i = mo.index
                random_index = random.randint(0,k-1)
                # if(random_index>= max_i):
                #     random_index+=1
                mo = jl[random_index]

            mo.pop()
            if(epoch % 2**7):

                vv = self.validate()
                va = vv[0]
                mmi = vv[1]
                mti = vv[2]
                
                va_list.append(va)
                x_index.append(epoch)
                # print(va)
                if(show_pross):
                    plt.plot(x_index, va_list,c='deeppink',ls='-')  ## 保存历史数据
                    plt.pause(0.1)
                    pass
                if(va==0):
                    sh_p = epoch


                pass_vote = jl[mti].time
                vote_ratio = pass_vote/epoch
                # print(vote_ratio)
                # 这个vote_ratio，是否可以与 保守概率p 比一比？？

                if(vote_ratio>pass_ratio):
                    if(va==1):
                        break
                    else:
                        failed = 1
                        break

        if(failed ==1):
            print('测试不通过，这样的及格线不合适，已强制继续练习。')


        if(va==1):
            print('成功收敛')
            print('收敛半径',sh_p)
            print('停止练习时的投票率',vote_ratio)
        else:
            print('算法失败了')
            print('实际的最优解',mmi,jl[mmi].means)
            print('机器的回答',mti,jl[mti].means)
        mmi = vv[1]
        mti = vv[2]
            
        print(jl[mti].time,epoch)

        ess_ratio = sh_p/epoch
        print('有效练习率',ess_ratio)

        if(show_pic):
            xz_index =list()
            z_index = list()
            for i,lhj_x in enumerate(jl):
                xz_index.append(i)
                z_index.append(lhj_x.time)
            plt.plot(xz_index, z_index,c='blue',ls='-')  ## 保存历史数据
        plt.pause(1000)

a = two_arm()
a.main()
