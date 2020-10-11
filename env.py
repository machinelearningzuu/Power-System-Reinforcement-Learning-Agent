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

        Epv_t = prev_state_values[0]
        Eb_t = prev_state_values[1]
        Ed_t = prev_state_values[2]

        if action == 0:
            Ac, Ad = 10, 0
            Eb_t1 = Eb_t + min(Ac, Ebmax - Eb_t)
        elif action == 1:
            Ac, Ad = 0, 10
            Eb_t1 = Eb_t - min(Ad, Ed_t - Epv_t, Eb_t - Ebmin)
        # elif action == 2:
        #     Ac, Ad = 0, 0
        #     Eb_t1 = Eb_t

        if Eb_t1 < Ebmin:
            Eb_t1 = Ebmin
        elif Eb_t1 > Ebmax:
            Eb_t1 = Ebmax

        demand = self.demands[time_step + 1]
        pv_value = self.pv_values[time_step + 1]

        new_state_values = (pv_value, Eb_t1, demand)
        new_state = self.state_space(*new_state_values)
        return new_state_values, new_state
