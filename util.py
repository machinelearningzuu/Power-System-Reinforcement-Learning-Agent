import os
import numpy as np
import pandas as pd
from variables import*

def preprocess_data():
    demand_data = pd.read_csv(demand_csv_path)
    data = pd.read_csv(data_csv_path)

    data = data[data.columns.values[:3].tolist() + [data.columns.values[-1]]]
    df = pd.merge(demand_data, data, on='Hour')
    df = df[data_columns]
    df = df.sort_values(["Month", "Day"], ascending = (True, True))

    df.to_csv(final_csv_path, index=False)

def get_data():
    if not os.path.exists(final_csv_path):
        preprocess_data()
    data = pd.read_csv(final_csv_path)
    pv_values = data['PV_component'].values
    demands = data['Demand']

def build_state_space(pv_value, Eb, demand):
    pv_bins = np.linspace(PVmin, PVmax, n_bins)
    pv_state = np.digitize(pv_value,pv_bins,right=True)

    demand_bins = np.linspace(Dmin, Dmax, n_bins)
    demand_state = np.digitize(demand,demand_bins,right=True)

    demand_bins = np.linspace(Dmin, Dmax, n_bins)
    demand_state = np.digitize(demand,demand_bins,right=True)

    Eb_bins = np.linspace(Ebmin, Ebmax, n_bins)
    Eb_state = np.digitize(Eb,Eb_bins,right=True)

    return str(pv_state) + str(Eb_state) + str(demand_state)
