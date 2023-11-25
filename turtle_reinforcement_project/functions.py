import random
import torch
import torch.nn as nn
from main import simulation
from reinforcement.env import Environment, Pitcher

def env_step(action):
    if action[0][0] == 15:
        timing = -1 #no swing
    else:
        timing = (action[0][0] * 10 + 5) + 5 * random.uniform(-1, 1)

    return timing

def get_reward(result):
    reward = 0
    if result == "strike":
        reward = -1
    elif result == "ball":
        reward = 1
    elif result == "Foul":
        reward = -0.5
    elif result == "out":
        reward = -2
    elif result == "single":
        reward = 2
    elif result == "double":
        reward = 3
    elif result == "triple":
        reward = 4
    elif result == "triple":
        reward = 5

    return reward

def get_env(action, state : Environment):

    timing = env_step(action)
    

    result = simulation(timing, state.pitcher, state)
    reward = get_reward(result)

    if result == "strike":
        terminated = state.strike_plus()
    elif result == "ball":
        terminated = state.ball_plus()
    elif result == "Foul":
        terminated = state.foul_plus()
    elif result == "out":
        terminated = state.out_plus()
    elif result == "single":
        terminated = state.single_plus()
    elif result == "double":
        terminated = state.double_plus()
    elif result == "triple":
        terminated = state.triple_plus()
    elif result == "homerun":
        terminated = state.homerun_plus()

    return state.env(), reward, terminated
