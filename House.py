class House:
    def __init__(self, area, floors, material):
        self.area = area
        self.floors = floors
        self.material = material
    
    def calculate_cost(self):
        cost_per_square_meter = {
            "wood": 1000,
            "brick": 1500,
            "concrete": 2000
        }
        cost = self.area * cost_per_square_meter.get(self.material, 0)
        return cost * self.floors

house1 = House(150, 2, "wood")
house2 = House(200, 3, "brick")


print(f"The cost of building House 1 is ${house1.calculate_cost()}.")
print(f"The cost of building House 2 is ${house2.calculate_cost()}.")
