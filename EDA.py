import pandas as pd

import os

import warnings
warnings.simplefilter('ignore')


def load_and_combining(folder_path, 
                       file_type = 'csv', 
                       data_sep = ';'):
    
    files = os.listdir(folder_path)
    df_combined = pd.DataFrame()
    count = 0

    for file in files:
        
        count += 1

        if file.endswith(file_type):

            file_path = folder_path + file
            df = pd.read_csv(file_path, 
                             sep = data_sep, 
                             parse_dates = True, 
                             index_col = 0)
            df.insert(loc = 0, 
                      column = 'weekday', 
                      value = file[:-4])
            df_combined = pd.concat([df_combined, 
                                     df], 
                                     axis = 0)
            
    return df_combined

df = load_and_combining('project_data/')

df.rename(columns = {'customer_no':'customer_id'}, 
          inplace = True)
df.sort_index(inplace=True)

weekdays = df['weekday'].unique()
max_id = 0
for day in weekdays:
    df.loc[df['weekday'] == day, ['customer_id']] = df.loc[df['weekday'] == day, ['customer_id']] + max_id
    max_id = df.loc[df['weekday'] == day, ['customer_id']].max()

df.reset_index(inplace = True)
df.set_index('customer_id', 
             inplace = True)

def drop_missing_checkout(df_group):
    if 'checkout' not in list(df_group):
        drop_row = df_group.name
        df.drop(index = drop_row, 
                inplace = True)
df.groupby('customer_id')['location'].apply(drop_missing_checkout)

df.reset_index(inplace = True)
df.set_index('timestamp', 
             inplace = True)

df = df.groupby('customer_id').resample('1min').ffill()

df['from'] = df.groupby(df['customer_id'])['location'].shift(+1)
df['from'] = df['from'].fillna('checkin')

P = pd.crosstab(index = df['from'], 
                columns = df['location'], 
                normalize = 0)

df.drop('customer_id', axis = 1, inplace = True)
df = df.reindex(columns = ['weekday', 'from', 'location'])

# df.to_csv('eda_data/supermarket_df')
# P.to_csv('eda_data/transition_df')

# print(df, P)