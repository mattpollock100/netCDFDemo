# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:47:18 2024

@author: mattp
"""

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import cartopy
import os
import cftime
from cartopy.util import add_cyclic_point
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

path_name = "C:/Users/mattp/OneDrive/Desktop/Climate Change MSc/"

file_name = "UKESM1_ssp585_2071-2100.cvdp_data.1850-2100.nc"

netCDF_file=xr.open_dataset(path_name + file_name,decode_times=False)

lat=netCDF_file['lat']
lon=netCDF_file['lon']

dataset = Dataset(path_name + file_name, mode='r')


plt.figure(figsize=(10,6)) 
projection = cartopy.crs.Robinson()     #specify the Robinson projection
ax = plt.axes(projection=projection)    #create axes
ax.coastlines()                         #add coastlines
ax.gridlines()                          #add some gridlines 
ax.add_feature(cartopy.feature.BORDERS) #add country borders


# Iterate through all variables
for var in dataset.variables:
   
    variable = dataset.variables[var]
   
    
    if variable.dimensions == ('lat', 'lon'):
        print(var)
        
        # load the variables themselves
        variable_name=var
        T=netCDF_file[variable_name]   
        
        #plot each variable
        plt.figure(figsize=(10,6)) 
        projection = cartopy.crs.Robinson()     #specify the Robinson projection
        ax = plt.axes(projection=projection)    #create axes
        ax.coastlines()                         #add coastlines
        ax.gridlines()                          #add some gridlines 
        ax.add_feature(cartopy.feature.BORDERS) #add country borders
        
        
        
        fig=T.plot.contourf(ax=ax, transform=cartopy.crs.PlateCarree(), \
                               cmap='coolwarm')#, \
                               #levels=np.linspace(-40,40,21))
    
        plt.title(var)
        
        #save an image file of each plot
        plt.savefig(path_name + 'Plots/' + var + '.png')
        plt.close()
    
netCDF_file.close()
