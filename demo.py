#! /usr/bin/env python
##############################
#   Program: demo.py
#
##############################
#   Author: J. Asplet
##############################
#   This is a example script for UoB Hydrogeology Course
#
#   If this script was doing something more interesting then you migh put some
#   longer premable here to give an overview of what it does
##############################
#   Import Statements - Useful to group these together at the top
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##############################
#   Standard Packages - all freely available

class Data:
    '''A python Class, the bedrock of Pythonic Object Oriented Programming
       within the class script the class is referred to as "self", which can
       be confusing at first but "self" is just a placeholder
    '''
    def __init__(self,a=10,b=2):
        '''The __init__ function. Required by all Classes (even if it doesnt do anything).
        This tell python what you want to happen what you initialise a Class (e.g. you might
        have something like Ex = demo.Data('somefile.txt') and in __init__ you then read in
        the data file ready to do soethingn with it.

        Here we are going to define some parameters to generate some data using random number
        genrators in numpy

        '''
        if (a == 0  or b == 0):
            print('Warning one of a: {:3d} or b: {:3d} is 0.'.format(a,b))
        self.a = a # Multplier. Sets range of values (e.g. if a=10 then value will range between 0 and 10)
        self.b = b # Shift. Shift values (e.g. if a=10,b=10 then values would range between 10 and 20)

        # Create data. We are going to make two sets of data, in different formats. As examples of how
        # to read in text files and grid files

        # Make rand arrays

        x = a*np.random.randn(20) + b
        #For fun, lets swap a and b round
        y = b*np.random.randn(20) + a
        print(x)
        # Make pandas DataFram
        df = pd.DataFrame(data={'X_Data': x,'Y_Data':y},index = [i for i in range(0,20)])
        # Write out the Dataframe
        df.to_csv('data.example',sep = ' ',index=False)
        # Altertative "purists" way
        with open('data.example2','w+') as writer:
            writer.write('X_Data Y_Data')
            for i,n in enumerate(x): # Iterate through values in x
                writer.write('{} {} \n'.format(x[i],y[i]))
        # Also make a grid file

        x = np.arange(-5, 5, 0.1)
        y = np.arange(-5, 5, 0.1)
        [X,Y] = np.meshgrid(x, y, sparse=True)
        Z = 10*np.sin(X**2 + Y**2) / (X**2 + Y*2)
        # write out this file
        np.savetxt('data.grid',Z,delimiter=',')

    def read_data(self):
        ''' Function to read in our example data. File names hard-coded in'''
        conv = {'Y_Data': lambda x: str(x) }

        self.df = pd.read_csv('data.example',delim_whitespace=True,converters=conv)

if __name__ == '__main__':
    print('Hello World. I am running from the command line')
