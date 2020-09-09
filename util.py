import os
import numpy as np
import pandas as pd
from variables import*

def preprocess_data():
    demand_data = pd.read_csv(demand_csv_path)
    data = pd.read_csv(data_csv_path)

    newdata = pd.DataFrame(np.repeat(data.values,4,axis=0))
    newdata.columns = data.columns

    min_len = min(len(newdata), len(demand_data))
    newdata = newdata[newdata.columns.values[:3].tolist() + [newdata.columns.values[-1]]]

    newdata = newdata.loc[:min_len]
    demand_data = demand_data.loc[:min_len]

    df = pd.concat([demand_data['Demand'], newdata], axis=1)
    df['PV_component'] = df['PV_component'].fillna(2.5)
    df = df[data_columns]
    df.to_csv(final_csv_path, index=False)

def create_time(Timestamp):
    date, time, _ = Timestamp.split(' ')
    month, day, _ = date.split('/')
    return month, day

def preprocess_demand_csv():
    df = pd.read_csv(demand_csv_path)
    df = df[df['Demand'].notna()]
    df = df[['Timestamp', 'Demand']]
    df.fillna(0)
    df['Month'], df['Day'] = zip(*df['Timestamp'].map(create_time))
    del df['Timestamp']
    df.to_csv(demand_csv_path, index=False)

def get_data():
    if not os.path.exists(final_csv_path):
        preprocess_data()
    data = pd.read_csv(final_csv_path)
    pv_values = data['PV_component'].values
    demands = data['Demand'].values
    hours = data['Hour'].values
    days = data['Day'].values
    months = data['Month'].values
    return pv_values, demands, hours, days, months

def build_state_space(pv_value, Eb, demand):
    pv_bins = np.linspace(PVmin, PVmax, n_bins)
    pv_state = np.digitize(pv_value,pv_bins,right=True)

    demand_bins = np.linspace(Dmin, Dmax, n_bins)
    demand_state = np.digitize(demand,demand_bins,right=True)

    Eb_bins = np.linspace(Ebmin, Ebmax, n_bins)
    Eb_state = np.digitize(Eb,Eb_bins,right=True)
    return int(str(pv_state) + str(Eb_state) + str(demand_state))
