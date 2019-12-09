import pandas as pd
import numpy as np

path = '~/data/'
# Load all the data
Client = pd.read_excel(path+'Client_info_20191118.xlsx',sheet_name='Sheet1')
TPA = pd.read_excel(path+'Copy_of_TPA_cash.xlsx',sheet_name='Sheet1')
Customer = pd.read_csv(path +'Customer_Data_Request_20191121.csv')
Perf = pd.read_csv(path +'Performance_Data_Request_20191204.csv')

# Client data columns selected to merge
Client_cols = ['Active',
 'Client ID',
 'Account Name',
 'Industry',
 'NAICS Code',
 'NAICS Description',
 'Broker',
 'TPA_x',
 'Launch Date',
 'Termination Date',
 'Affiliate/Fed Gov?',
 'Cash']

Client = Client.merge(TPA,how='left',left_on='Client ID',right_on='HOST ID')
Customer = Customer.merge(Client[Client_cols],how='left',left_on='Unique_Company_ID',right_on='Client ID')
Perf = Perf.merge(Customer, how='left',on='Unique_Customer_ID')

# Data Preprocessing of Perf
Perf['Year_and_Month'] = pd.to_datetime(Perf['Year_and_Month'].astype(str), format = '%Y%m')
Perf['YQ'] = pd.PeriodIndex(Perf['Year_and_Month'], freq='Q')