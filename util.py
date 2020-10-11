import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from variables import*

def preprocess_data():
    demand_data = pd.read_csv(demand_csv_path)
    solar_data = pd.read_csv(data_csv_path)

    solar_data = solar_data[['Timestamp', 'PV_component']]
    demand_data = demand_data[['Timestamp', 'Demand']]

    df_final = pd.merge(demand_data, solar_data, on='Timestamp')
    df_final['PV_component'] = df_final['PV_component'].fillna(2.5)
    df_final['Demand'] = df_final['Demand'].fillna(0)

    df = preprocess_final_df(df_final)
    df = df[data_columns]
    df.to_csv(final_csv_path, index=False)

def create_time(Timestamp):
    date, time, time_half = Timestamp.split(' ')
    month, day, _ = date.split('/')
    hour, minute, second = time.split(':')
    hour = int(hour)
    if time_half.strip().lower() == 'am':
        if hour == 12:
            hour = 0
    elif time_half.strip().lower() == 'pm':
        if hour != 12:
            hour = hour + 12
    return month, day, hour

def preprocess_final_df(df):
    df = df[['Timestamp', 'Demand', 'PV_component']]
    df['Month'], df['Day'], df['Hour'] = zip(*df['Timestamp'].map(create_time))
    del df['Timestamp']
    return df
    
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

def load_dnn_data():
    df = pd.read_csv(solar_dnn_csv)
    df = df[solar_dnn_cols]
    data  = df.dropna(axis = 0, how ='any')
    X = data[solar_dnn_cols[:-1]].values

    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)
    Y = data[solar_dnn_cols[-1]].values
    return X, Y
