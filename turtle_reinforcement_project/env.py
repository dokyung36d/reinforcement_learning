import random
import torch
import torch.nn as nn
from pitcher_data import all_pitcher_data

class Environment():
    def __init__(self) -> None:
        self.total_score = 0
        self.strike = 0
        self.ball = 0
        self.out = 0
        self.curr_base = [0, 0, 0] #각 1,2,3 루
        self.pitcher = Pitcher()
    
    def env(self):
        observation = [self.strike,self.ball, self.out,
                self.curr_base[0], self.curr_base[1], self.curr_base[2]]
        observation.extend(self.pitcher.fast_conditional)
        return observation
    
    def set_env(self, observation):
        self.strike = observation[0]
        self.ball = observation[1]
        self.out = observation[2]
        self.curr_base = [observation[3], observation[4], observation[5]]
        
    
    def strike_plus(self):
        terminate = False
        if self.strike == 2:
            if self.out == 2:
                self.strike, self.ball, self.out, self.curr_base = 0, 0, 0, [0, 0, 0]
                terminate = True
            else:
                self.out += 1
        else:
            self.strike += 1

        return terminate

    def ball_plus(self):
        terminate = False
        if self.ball == 3:
            if self.curr_base[0] == 0: #1루가 비어있는 경우
                self.curr_base[0] = 1
            elif self.curr_base[0] == 1 and self.curr_base[1] == 1: #1, 2루가 채워 있는 경우
                self.curr_base[2] = 1
            elif self.curr_base[0] == 1 and self.curr_base[1] == 1 and self.curr_base[2] == 1:
                self.total_score += 1
            elif self.curr_base[0] == 1 and self.curr_base[2] == 1:
                self.curr_base[1] = 1
            elif self.curr_base[0] == 1:
                self.curr_base[1] = 1
        else:
            self.ball += 1
        return terminate

    def foul_plus(self):
        terminate = False
        if self.strike == 0 or self.strike == 1:
            self.strike += 1

        return terminate

    def out_plus(self):
        terminate = False
        if self.out == 2:
            self.strike, self.ball, self.out, self.curr_base = 0, 0, 0, [0, 0, 0]
            terminate = True
        else:
            self.out += 1

        return terminate

    def single_plus(self):
        terminate = False
        self.strike = 0
        self.ball = 0
        if self.curr_base[2] == 1:
            self.total_score += 1
            self.curr_base[2] = 0
        
        if self.curr_base[1] == 1:
            self.curr_base[2] = 1
            self.curr_base[1] = 0
        
        if self.curr_base[0] == 1:
            self.curr_base[1] = 1
            #self.curr_base[0] = 1 --> 할 필요없음, 어차피 안타친 타자가 1루에 들어감
        return terminate

    def double_plus(self):
        terminate = False
        self.strike = 0
        self.ball = 0
        if self.curr_base[2] == 1:
            self.total_score += 1
            self.curr_base[2] = 0
        
        if self.curr_base[1] == 1:
            self.total_score += 1
            self.curr_base[1] = 0
        
        if self.curr_base[0] == 1:
            self.curr_base[2] = 1
            self.curr_base[1] = 1
            self.curr_base[0] = 0
        return terminate

    def triple_plus(self):
        terminate = False
        self.strike = 0
        self.ball = 0
        if self.curr_base[2] == 1:
            self.total_score += 1
            self.curr_base[2] = 0
        
        if self.curr_base[1] == 1:
            self.total_score += 1
            self.curr_base[1] = 0
        
        if self.curr_base[0] == 1:
            self.total_score += 1
            self.curr_base[0] = 0
            self.curr_base[2] = 1
        
        return terminate

    def homerun_plus(self):
        self.strike = 0
        self.ball = 0
        terminate = False
        if self.curr_base[2] == 1:
            self.total_score += 1
            self.curr_base[2] = 0
        
        if self.curr_base[1] == 1:
            self.total_score += 1
            self.curr_base[1] = 0
        
        if self.curr_base[0] == 1:
            self.total_score += 1
            self.curr_base[0] = 0

        self.total_score += 1
        return terminate

class DQN(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.timing = 0 #0 ~ 150
        self.swing = None #Boolean
        self.dim = 11
        self.hidden_dim = 32
        self.out_dim = 16 #0~150가능 -> 각 10당 할당, 나머지 하나는 no swing
        self.linear1 = nn.Linear(self.dim, self.hidden_dim)
        self.linear2 = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.linear3 = nn.Linear(self.hidden_dim, self.out_dim)
        #이후 각 구간으로 나눈 다음 약간의 random성을 넣으면 좋을 듯
        #만약 0~15이면 0~10까지 할당 +-5값은 random하게 줌. 나머지 하나는 no swing
        self.gelu = nn.GELU()


    #forward에서 Standard Normal Distribution이후 해당 값을 변환
    def forward(self, x): #x에는 env, 현재 투수
        x = self.gelu(self.linear1(x))
        x = self.gelu(self.linear2(x))
        x = self.gelu(self.linear3(x))

        return x #output의 경우 최종으로 변환하여 -50~200으로 하는 것이 좋을 듯. 
    #Monte Carlo 방식으로 학습하면 좋을 듯?

class Pitcher():
    def __init__(self) -> None: #추후 투수의 conditional에 맟춰야 함.
        self.fast_conditional = all_pitcher_data[random.randint(0, 19)]
        # self.fast_conditional = [0.507, 0.418, 0.361, 0.674, 0.502]
        #예시 : [50.7, 41.8, 36.1, 67.4, 50.2]

    def return_trajectory(self, env : Environment): #여기서 상황에 따라 자세히 구현해야 함.
        random_number = random.random()

        if env.strike == 0 and env.ball == 0:
            if self.fast_conditional[0] < random_number:
                return "fastball"
            else:
                return "curve"
        
        if env.strike > env.ball:
            if self.fast_conditional[2] < random_number:
                return "fastball"
            else:
                return "curve"
            
        if env.strike < env.ball:
            if self.fast_conditional[3] < random_number:
                return "fastball"
            else:
                return "curve"
            
        if env.strike == env.ball:
            if self.fast_conditional[4] < random_number:
                return "fastball"
            else:
                return "curve"
        
        # if self.fast_prob < random_number:
        #     return "fastball"
        # else:
        #     return "curve"

    def return_prob(self):
        return self.fast_conditional
    
class Learning():
    def __init__(self):
        pass

# def env_step(action, env : Environment):
#     if action[0][0] == 16:
#         timing = -1 #no swing
#     else:
#         timing = (action[0][0] * 10 + 5) + 5 * random.uniform(-1, 1)

# def get_reward(result):
#     reward = 0
#     if result == "strike":
#         reward = -1
#     elif result == "ball":
#         reward = 1
#     elif result == "Foul":
#         reward = -0.5
#     elif result == "out":
#         reward = -2
#     elif result == "single":
#         reward = 2
#     elif result == "double":
#         reward = 3
#     elif result == "triple":
#         reward = 4
#     elif result == "triple":
#         reward = 5

# def get_env(action, state : Environment):
#     timing = env_step(action)

#     result = simulation(timing)
#     reward = get_reward(result)

#     if result == "strike":
#         terminated = state.strike_plus()
#     elif result == "ball":
#         terminated = state.ball_plus()
#     elif result == "Foul":
#         terminated = state.foul_plus()
#     elif result == "out":
#         terminated = state.out_plus()
#     elif result == "single":
#         terminated = state.single_plus()
#     elif result == "double":
#         terminated = state.double_plus()
#     elif result == "triple":
#         terminated = state.triple_plus()
#     elif result == "homerun":
#         terminated = state.homerun_plus()

#     return state.env, reward, terminated


# agent = DQN()