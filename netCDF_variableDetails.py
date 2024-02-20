# -*- coding: utf-8 -*-


from netCDF4 import Dataset

# Open a NetCDF file
path_name = "C:/Users/mattp/OneDrive/Desktop/Climate Change MSc/"

file_name = "UKESM1_ssp585_2071-2100.cvdp_data.1850-2100.nc"

dataset = Dataset(path_name + file_name, mode='r')





# Iterate through all variables
for var in dataset.variables:
   
    variable = dataset.variables[var]
    
    #if variable.dimensions == ('lat', 'lon'):
        
    # Print main details of the variable
    print(f"Variable: {var}")
    print(f"Dimensions: {variable.dimensions}")
    #print(f"Shape: {variable.shape}")
    #print(f"Data type: {variable.dtype}")

    # If the variable has a long_name attribute, also print that
    # otherwise move to the next one
    try:
        attr_name= 'long_name'
        attr_value = variable.getncattr(attr_name)    
        print(f"{attr_name}: {attr_value}")
        print("\n")
    except:

        print("\n")  
        

# Close the dataset
dataset.close()
