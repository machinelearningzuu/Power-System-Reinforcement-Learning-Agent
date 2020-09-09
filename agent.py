import os
import random
import numpy as np
import matplotlib.pyplot as plt
from variables import*
from util import build_state_space, get_data

from env import Environment

class Agent(object):
    def __init__(self):
        self.env = Environment()

        low_state_value = self.env.state_space(PVmin, Ebmin, Dmin)
        high_state_value = self.env.state_space(PVmax, Ebmax, Dmax)

        num_states = high_state_value - low_state_value + 1
        num_actions = 2
        if os.path.exists(q_table_path):
            print("Q table Loading !!!")
            self.load_q_table()
        else:
            print("Q table Initializing !!!")
            self.q_table = np.random.uniform(low = -1, high = 1 , size = (num_states,num_actions))

    def train(self):
        total_rewards_in_days = []
        total_time_steps = 0
        for day in range(num_days):
            day_reward = 0
            state_values, state = self.env.reset()
            while (self.env.hours[total_time_steps] != 23):
                if random.uniform(0,1) < eps:
                    action =  self.env.sample_action()
                else:
                    action =  np.argmax(self.q_table[state,:])

                Epv = state_values[0]
                Eb  = state_values[1]
                Ed  = state_values[2]
                E_grid = Ed - Epv + Eb

                reward = c*max(E_grid, 0) + p*min(E_grid, 0)
                reward = reward * 0.00001
                new_state_values, new_state = self.env.step(total_time_steps, state_values, action)

                self.q_table[state,action] = (1 - learning_rate) * self.q_table[state,action] \
                                                + learning_rate * (reward + discount_factor * np.max(self.q_table[new_state,:]))

                day_reward -= reward
                state = new_state
                state_values = new_state_values
                total_time_steps += 1
            total_time_steps += 1
            total_rewards_in_days.append(day_reward)
        Agent.plot_cumulative_costs(total_rewards_in_days,num_days)

    @staticmethod
    def plot_cumulative_costs(total_rewards_in_days,num_days):
        # plot the cumulative average rewards
        cum_rewards = np.cumsum(total_rewards_in_days)
        cum_average_reward = cum_rewards / np.arange(1,num_days+1)

        fig = plt.figure()
        plt.plot(cum_average_reward)
        fig.suptitle('Power System Agent Cost Analysis', fontsize=20)
        plt.xlabel('days')
        plt.ylabel('Cost')
        fig.savefig(cum_cost_path)

    def save_q_table(self):
        np.save(q_table_path, self.q_table)

    def load_q_table(self):
        self.q_table = np.load(q_table_path)

if __name__ == "__main__":
    agent =  Agent()
    agent.train()
    agent.save_q_table()