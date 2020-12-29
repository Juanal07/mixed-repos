import gym

env = gym.make("Taxi-v3").env

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

state = env.encode(3, 1, 2, 0)  # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
env.render()

env.P[328]

