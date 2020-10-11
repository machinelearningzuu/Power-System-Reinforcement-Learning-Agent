Ebmin = 20
Ebmax = 100

PVmin = 0
PVmax = 1.111

Dmin = 2
Dmax = 340

n_bins = 10

p = 22
learning_rate = 1e-4
cost_lr = 1e-2
eps = 0.6
discount_factor = 0.99
num_days = 365

initial_state = (PVmin, Ebmax, Dmin)
initial_action = 2 # (0 - charging, 1 - discharging, 2 - Nothing)

demand_csv_path = 'Data/demand.csv'
data_csv_path = 'Data/solar.csv'
final_csv_path = 'Data/final_csv.csv'

q_table_path = 'weights/power system agent q learning.npy'
cum_cost_path = 'weights/power_system_agent.png'
Egrid_path = 'weights/E grid effiency.png'
data_columns = ['Month','Day','Hour','PV_component','Demand']

#Solar DNN estimator
solar_dnn_csv = 'DNN/solar_forecasting.csv'
solar_dnn_cols = ['Wind Speed (m/s)','Plane of Array Irradiance (W/m^2)','Cell Temperature (C)','AC System Output (W)']
dim1 = 32
dim2 = 1
batch_size = 64
validation_split = 0.2
verbose=1
epochs = 100
solar_weights = 'weights/solar_model.h5'
loss_img = 'weights/solar_loss.png'