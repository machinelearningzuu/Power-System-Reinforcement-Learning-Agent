import numpy as np
from variables import*
from util import build_state_space, get_data

class Environment(object):
    def __init__(self):
        self.state_space = build_state_space

        pv_values, demands, hours, days, months = get_data()
        self.pv_values = pv_values
        self.demands = demands
        self.hours = hours
        self.days = days
        self.months = months

    def reset(self):
        return initial_state, self.state_space(*initial_state)

    @staticmethod
    def sample_action():
        return np.random.choice([0,1])

    def step(self, time_step, prev_state_values, action):
        Ac = 1 if action == 0 else 0
        Ad = 1 if action == 1 else 0

        Eb_t = prev_state_values[1]
        Eb_t1 = Eb_t + (efficiency *  Ac) - (Ad / efficiency)
        if Eb_t1 < Ebmin:
            Eb_t1 = Ebmin
        elif Eb_t1 > Ebmax:
            Eb_t1 = Ebmax

        demand = self.demands[time_step + 1]
        pv_value = self.pv_values[time_step + 1]

        new_state_values = (pv_value, Eb_t1, demand)
        new_state = self.state_space(*new_state_values)
        return new_state_values, new_state




















# print(Environment().reset())