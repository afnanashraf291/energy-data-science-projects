import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


load = [100, 50, 30, 200, 150, 60]

print("Helo world")
print("Python version", sys.version_info.major, "\n" \
"Numpy version__", np.__version__, "\n" \
"Pandas version :", pd.__version__)
print("Electricity demand in different years:", load)
print("MAX of Demand", max(load))
print("Min of load", min(load))
#%%
name = "Afnan"
age= 21
country = "Pakistan"
city = "Frankfurt"
print(f"My name is: {name}, I am {age} years old. I am from {country} and currently lives in {city}")
#%%
electricity_price = 0.30 #euro/Kwh 
time = 8 #hours
power_consumed= 5 #KW

energy_consumption= time*power_consumed
electricity_cost = energy_consumption*electricity_price

print(f"""The machine has consumed {energy_consumption} Kwh in {time} 
hours that cost the company {electricity_cost} euros""")

#%%
power = 10
hours = 6
price = 0.35

total_electricity_cost= power*hours*price
print(f"total electricity cost is {total_electricity_cost} in euros")
