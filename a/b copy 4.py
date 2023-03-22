# 设计这样一个游戏

'''
    世界是二维 4*4 世界中有奖励点与惩罚点，限制游戏时长为 500 ，如果没有结束则强制结束 ，奖励为0
    如果遇到了奖励点，则游戏结束 ，奖励为1 如果遇到了惩罚点，则奖励为0，游戏也结束 。


    特点，稀疏奖励。

    玩法1    不固定奖励点位，但主体能接受到奖励点的位置状态
    玩法2    迷宫，不知道奖励点在哪，主体只能去摸索。


    

    状态，奖励点的位置，主体当前 的位置
    行为 上下左右四种移动。

    我觉得可以用cnn来看图，而且，能用cnn 就应该能用自注意。

    cnn 自注意的意义，其实只用全连接就能解决，但引入 它们，算法会更快地收敛。

'''


import random
import plt_scatter

class one_piece():


    def __init__(self):
        self.agent_list = list()
        self.paint = 0

        # target = random.randint(0,16-1)
        # target = 2
        # agent_pos = random.randint(0,16-1)
        # agent_pos = 0


        self.patience = 32
        # self.step = 0
        self.hp = self.patience
        
        self.terminate = 0
        self.score = 0
        width = 4
        hight = 4

        tr = random.randint(0,hight-1)
        tc = random.randint(0,width-1)
        ar = random.randint(0,hight-1)
        ac = random.randint(0,width-1)

        # ar = tr
        # ac = tc


        target = tr *width + tc            
        agent_pos = ar * width + ac




        self.state = [target,agent_pos] # 目标在0 主体在16

        # 打印
        # print('self.state',self.state)
        print(tr,tc)
        print(ar,ac)


        if(self.paint == 1):
                
            self.plt = plt_scatter.plt_scatter()

            self.plt.x = ac
            self.plt.y = ar

            self.plt.tx = tc
            self.plt.ty = tr

            self.plt.paint()



    def world_change(self):
        
        for agnet_index,agent in enumerate(self.agent_list):
            action = agent.action
            
            agent_pos = self.state[1]
            # print(agent_pos)
            
            target = self.state [0]
            if(target == agent_pos):
                # print('game_over')
                print('win',self.hp)
                self.terminate = 1
                # self.score = 1
            else:
                if(self.hp<=0):
                    print('loose',self.hp)
                    self.terminate = 1
            
            width = 4
            hight = 4
            
            # 行坐标，列坐标
            ar = agent_pos // width
            ac = agent_pos % hight

            
            # print('行，列',ar,ac)

            if(action== 0):
                # print('上移')
                if (ar!=0):
                    # print('需要移动')
                    ar -=1

            elif(action== 1):
                # print('下移')
                if (ar!=3):
                    ar +=1
            elif(action==2):
                if(ac != 0):
                    ac -= 1
            elif(action == 3):
                if(ac !=3):
                    ac += 1

            self.hp -=1

            

            # print('行，列',ar,ac)

            agent_pos = ar * width + ac
            self.state[1] = agent_pos

        if(self.paint == 1):

            w =self
            if(w.terminate==0):
                self.plt.x = ac
                self.plt.y = ar
                self.plt.paint()


        

    def run(self):
        w = self
        al = w.agent_list
        a = al[0]
                
        
        while(1):
            a.action_f()
            w.world_change()
            if(w.terminate==1):
                break
        if(self.paint == 1):
            
            self.plt.remain()
        
class agent():

    def action_f(self):
        action = 0

        state = a.world.state

        action = random.randint(0,4-1)
        self.action = action
        # return action



w = one_piece()
a = agent()
a.world = w
w.agent_list.append(a)
w.run()