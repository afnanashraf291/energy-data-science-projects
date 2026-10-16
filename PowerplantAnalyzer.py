PLANTS = {
    "Coal": {
        "capacity": 200,          # MW
        "efficiency": 0.40,
        "emission_factor": 0.8,   # tCO2/MWh
        "FLH": 5000               # hours/year
    },

    "Gas": {
        "capacity": 150,
        "efficiency": 0.55,
        "emission_factor": 0.4,
        "FLH": 3000
    },

    "Solar": {
        "capacity": 100,
        "efficiency": 1.0,
        "emission_factor": 0.0,
        "FLH": 1000
    },

    "Wind": {
        "capacity": 80,
        "efficiency": 1.0,
        "emission_factor": 0.0,
        "FLH": 2500
    }
}


class PowerPlantAnalyzer:

    def __init__(self, name, capacity, flh, efficiency, emission_factor, price):
        self.name=name
        self.capacity=capacity
        self.flh=flh
        self.efficiency=efficiency
        self.emission_factor=emission_factor
        self.price=price

    def annual_production(self):
        return self.capacity*self.flh

    def annual_reveneu_calculator(self):
        energy= self.annual_production()
        annaul_revenue= energy*self.price
        return annaul_revenue

    def calculate_emissions(self):
        energy=self.annual_production()
        emissions= energy*self.emission_factor
        return emissions

    def calculate_fuel_energy(self):
        annual_energy=self.annual_production()
        fuel_energy=annual_energy/self.efficiency
        return fuel_energy


coal=PowerPlantAnalyzer("Coal", 200, 4500, 0.35, 0.5, 0.17)
#annual_production=coal.annual_production()
#print(type(annual_production))
print(f"""coal has annually produced {coal.annual_production()} Mwh
with reveneu of {coal.annual_reveneu_calculator()} euros
having emissions of {coal.calculate_emissions()} tonnes of co2""")    