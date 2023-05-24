from EDA import P
from faker import Faker
from numpy.random import choice

fake = Faker()

class Customer():

    '''
    
    single customer that moves through the supermarket
    
    '''

    def __init__(self, name, P = P, budget = 100):
        self.name = name
        self.state = 'checkin'
        self.budget = budget
        self.locations = P.columns
        self.transition = ['checkin']
        self.status = []
    
    def next_state(self):

        '''
        
        following the transition probability append to the transition list the next customer's location
        
        '''

        self.state = choice(self.locations, p = P.loc[self.state])
        self.transition.append(self.state)

    def is_active(self):

        '''
        
        returns True if the customer hasn't reach the checkout yet, 
        or False if the customer reach the checkout area
        
        '''
        
        if self.state != 'checkout':
            self.status = True
        if self.state == 'checkout':
            self.status = False