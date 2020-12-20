import gym

env = gym.make("Taxi-v3").env
state = env.reset()
env.render()
env.close()

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

print('\x1b[31mRED' + '\x1b[33mYELLOW' +  '\x1b[32mGREEN' + '\x1b[35mPINK' + '\x1b[0m' + '\n')
