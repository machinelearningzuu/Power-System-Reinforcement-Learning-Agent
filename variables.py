Ebmin = 0
Ebmax = 10

PVmin = 0
PVmax = 3.003645

Dmin = 1.5
Dmax = 6.5

n_bins = 10
efficiency = 0.7

c = 20
p = 15
learning_rate = 10e-3
eps = 0.9
discount_factor = 0.9
num_days = 365

initial_state = (PVmin, Ebmax, 2.5)
initial_action = 1 # (charging, discharging)

demand_csv_path = 'demand.csv'
data_csv_path = 'solar op.csv'
final_csv_path = 'final_csv.csv'
q_table_path = 'power system agent q learning.npy'

data_columns = ['Month','Day','Hour','PV_component','Demand']
