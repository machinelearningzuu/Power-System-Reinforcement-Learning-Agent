import numpy as np
from variables import*
from util import build_state_space

class Environment(object):
    def __init__(self):
        self.state_space = build_state_space

    def reset(self):
        return self.state_space(*initial_state)

    @staticmethod
    def sample_action():
        return np.random.choice([0,1], 2, replace=False)

    def step(self, prev_state_values, action):
        Ac = action[0]
        Ad = action[1]

        Eb_t = prev_state_values[1]
        Eb_t1 = Eb_t + (efficiency *  Ac) - (Ad / efficiency)

        new_state_values = ()




















# print(Environment().reset())