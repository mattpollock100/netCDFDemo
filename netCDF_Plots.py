import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

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

# load the variables themselves
variable_name='tas_spatialmean_ann' 
T=netCDF_file[variable_name]   


plt.figure(figsize=(10,6)) 
projection = cartopy.crs.Robinson()     #specify the Robinson projection
ax = plt.axes(projection=projection)    #create axes
ax.coastlines()                         #add coastlines
ax.gridlines()                          #add some gridlines 
ax.add_feature(cartopy.feature.BORDERS) #add country borders



fig=T.plot.contourf(ax=ax, transform=cartopy.crs.PlateCarree(), \
                       cmap='coolwarm')#, \
                       #levels=np.linspace(-40,40,21))
    
plt.title(variable_name)


netCDF_file.close()
