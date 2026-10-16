demand = [100, 80, 150, 230]
solar = [50, 80, 100, 40]
wind = [30, 20, 40, 50]
gas_capacity= 60
battery= 10
battery_capacity=100
gas_emission_factor = 0.40  # tonnes CO2/MWh
grid_emission_factor = 0.35  # tonnes CO2/MWh
gas_price=40
grid_price=60
Re_generation=[]
battery_level=[]
gas_gen=[]
grid_imports=[]
hourly_emissions=[]
hourly_cost=[]

for i in range(len(demand)):
    gas_dispatch=0
    grid_dispatch=0
    emissions=0
    cost=0
    re_gen= solar[i]+wind[i]
    if re_gen<demand[i]:
        rem_demand= demand[i] - re_gen
        battery_discharge=min(rem_demand, battery)
        battery=battery-battery_discharge
        battery_level.append(battery)
        re_and_battery=re_gen+battery_discharge
        if re_and_battery<demand[i]:
            demand_unmet=demand[i]-(re_gen+battery_discharge)
            gas_dispatch=min(gas_capacity, demand_unmet)
            emissions=emissions+gas_dispatch*gas_emission_factor
            cost=cost+gas_dispatch*gas_price
        if demand[i]>(re_gen+gas_dispatch+battery_discharge):
            grid_dispatch=demand[i]-(re_gen+gas_dispatch)
            emissions=emissions+grid_dispatch*grid_emission_factor
            cost=cost+grid_dispatch*grid_price
    
        # elif (re_gen+discharge)<demand[i]:
        #     print("gas dispatch")
        #     gas_dispatch=demand[i]- (re_gen+discharge)
        #     gas_gen.append(gas_dispatch)
    else:
        charge=re_gen-demand[i]
        available_space = battery_capacity - battery
        battery=battery + min(available_space, charge)
        battery_level.append(battery)
    Re_generation.append(re_gen)
    gas_gen.append(gas_dispatch)
    grid_imports.append(grid_dispatch)
    hourly_emissions.append(emissions)
    hourly_cost.append(cost)
print(battery_level, gas_gen,grid_imports, hourly_emissions)
Re_share=sum(Re_generation)/sum(demand)*100
print(f"""total demanad is: {sum(demand)}
total RE generation is: {sum(Re_generation)}
total gas generated : {sum(gas_gen)}
total grid imports are : {sum(grid_imports)}
total emissions are :{sum(hourly_emissions)}
total electricity cost is :  {sum(hourly_cost)}
Re share is : {Re_share}""")