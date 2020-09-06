Ebmin = 0.4
Ebmax = 2

PVmin = 0
PVmax = 3.0

Dmin = 1.5
Dmax = 6.5

n_bins = 10
efficiency = 0.7

c = 20
p = 15

initial_state = (PVmin, Ebmax, 2.5)
initial_action = [0, 1] # (charging, discharging)

demand_csv_path = 'demand.csv'
data_csv_path = 'solar op.csv'
final_csv_path = 'final_csv.csv'

data_columns = ['Month','Day','Hour','PV_component','Demand']
