# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:15:45 2024

@author: mattp
"""

from netCDF4 import Dataset

# Open a NetCDF file
path_name = "C:/Users/mattp/OneDrive/Desktop/Climate Change MSc/"

file_name = "UKESM1_ssp585_2071-2100.cvdp_data.1850-2100.nc"

dataset = Dataset(path_name + file_name, mode='r')



# Iterate through all variables
for var in dataset.variables:
   
    variable = dataset.variables[var]

    
    # Print common details of the variable
    print(f"Variable: {var}")
    print(f"Dimensions: {variable.dimensions}")
    print(f"Shape: {variable.shape}")
    print(f"Data type: {variable.dtype}")
    
    
    # Iterate and print all attributes of the variable
    for attr_name in variable.ncattrs():
        attr_value = variable.getncattr(attr_name)
        print(f"{attr_name}: {attr_value}")
    
    #New line 
    print("\n")
    
    
# Close the dataset
dataset.close()