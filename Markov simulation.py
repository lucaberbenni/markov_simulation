import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import imageio

import warnings
warnings.simplefilter('ignore')

'''

import simulation dataframe

'''

df = pd.read_csv('supermarket_data/simulation.csv', 
                 parse_dates = True, 
                 index_col= 0)

'''

loop through every minute and plot the customers for every location, 
save all the plots as .png files

'''

for minute in df['date'].unique():
    fig, ax = plt.subplots(figsize = (12, 7))
    data = df[df['date'] == minute]
    customers = data['location'].value_counts().sort_index()
    sns.barplot(data = data, 
                x = customers.index, 
                y = customers.values,   
                palette = 'muted', 
                ax = ax)
    ax.set_xlabel('Locations')
    ax.set_ylabel('Customers')
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(0, 20)
    plt.title(f'{minute}')
    plt.savefig(f'simulation_data/simulation{minute}.png')
    plt.close()

'''

create a gif concatenating all the .png files

'''

images = []
for minute in df['date'].unique():
    filename = 'simulation_data/simulation{}.png'.format(minute)
    images.append(imageio.imread(filename))
imageio.mimsave('output/simulation.gif', 
                images, 
                fps = 7)
# print(df)