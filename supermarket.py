import pandas as pd
import numpy as np

import faker as faker
from customers import *
import datetime

class Supermarket():
    
    '''
    
    multiple customer instances that are currently in the supermarket
    
    '''

    def __init__(self):

        self.start_time = datetime.datetime(2023, 4, 17, 7, 0)
        self.end_time = datetime.datetime(2023, 4, 17, 22, 0)
        self.open_time= []
        self.customers_list = []
        self.status = []
        self.data_dict = {'date': [], 'id': [], 'location': []}
    
    def run(self):

        '''
        
        open the supermarket, add new customers and let them move every minute;
        then create a dataframe with the datas for all customers and save it as a csv file

        '''
        
        self.current_time = self.start_time
        while self.current_time <= self.end_time:
            self.open_time.append(self.current_time.strftime("%H:%M"))
            self.add_new_customers()
            self.move_customers()
            self.current_time += datetime.timedelta(minutes = 1)
        df = pd.DataFrame(self.data_dict)
        df.to_csv('supermarket_data/simulation.csv')
    
    def add_new_customers(self):
        
        '''
        
        randomly create new customers
        
        '''
       
        for i in range(np.random.randint(0, 10)):
                cust = Customer(fake.name())
                self.customers_list.append(cust)
        
    def move_customers(self):
         
         '''
         
         move customers to next location if is active,
         adding the datas to a dictionary
         
         '''
         for customer in self.customers_list:
            customer.is_active()
            if customer.status != False:
                customer.next_state()
                self.add_data(customer)

    def add_data(self, customer):

        '''
        
        function append datas to a dictionary
        
        '''

        self.data_dict['date'].append(self.current_time)
        self.data_dict['id'].append(customer.name)
        self.data_dict['location'].append(customer.state)
		            
supermarket = Supermarket()
supermarket.run()