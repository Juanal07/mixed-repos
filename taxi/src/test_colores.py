import gym
import numpy as np

env = gym.make("Taxi-v3").env

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

state = env.encode(0, 0, 4, 0)  # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
env.render()

print(env.P[state])
