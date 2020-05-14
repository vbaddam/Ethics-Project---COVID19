#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:08:33 2020

@author: anikat
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def analyze_apple_mobility(regions_to_check):
    data_path='applemobilitytrends-2020-05-03.csv'
    regions=['New York City', 'New York']

    data=pd.read_csv(data_path,delimiter=',')

    data=data[data['region'].isin(regions_to_check)].reset_index()

    cols=data.columns
    print(data.shape)
    #print(len(cols))
    stepsize=5
    for ix, row in data.iterrows():
        print(row.iloc[4:])
        fig, ax = plt.subplots()
        plt.plot(row.iloc[5:].values)
        ax.xaxis.set_ticks(np.arange(0, len(data.columns)-5, stepsize))
        #ax.set_xticklabels(cols[5:])
        plt.title(row['region']+' '+row['transportation_type'])
        plt.show()

def analyze_descreta():
    data_path='DL-us-m50.csv'
    data=pd.read_csv(data_path,delimiter=',')
    data=data[data['admin1']=='New York']
    
    print(data.shape)
    data=data.drop(columns=['country_code','admin_level','admin1'])
    
    cols=data.columns
    print(len(cols))
    print(data.columns)
    region=data['admin2'].values
    #fig, ax = plt.subplots()
    flag=False
    for ix, row in data.iterrows():
        #print(row.iloc[2:])
        filename='mobility_fig_sample/'+'NY-'
        title='NY-'+str(int(row['fips']))
        if flag:
            filename+=row['admin2']
        plt.plot(row.iloc[2:].values)
        plt.title(title)
        plt.ylim(0,7)
        plt.savefig(filename+'.png')
        plt.show()
        flag=True

    
    #plt.legend(region)
    #ax.set_xticklabels(cols[5:])
    #plt.title('NY region mobility Descreta')
    #plt.legend(loc=[1.01,0.05])
    #plt.show()

    
regions_to_check=['New Jersey','California','Virginia', 'Maryland','Georgia','Texas']
analyze_apple_mobility(regions_to_check)

#analyze_descreta()