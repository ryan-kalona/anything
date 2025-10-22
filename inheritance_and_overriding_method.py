class appliance:
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self):
        print(f"the {self.brand} appliance is now on.")

    def turn_off(self):
        print(f"the {self.brand} appliance is now off.")

class washingmachine(appliance):
    def __init__(self, brand, load_capacity):
        super().__init__(brand)
        self.load_capacity = load_capacity

    def turn_on(self):
        super().turn_on()
        print(f"{self.brand} washing machine is filling water and starting a wash cycle.")

class microwave(appliance):
    def __init__(self, brand, power_level):
        super().__init__(brand)
        self.power_level = power_level

    def turn_on(self):
        super().turn_on()
        print(f"{self.brand} microwave is heating food at power level {self.power_level}.")

class refrigerator(appliance):
    def __init__(self, brand, temperature):
        super().__init__(brand)
        self.temperature = temperature

    def turn_on(self):
        super().turn_on()
        print(f"{self.brand} refrigerator is cooling to {self.temperature}°C.")

if __name__ == "__main__":
    appliances = [
        washingmachine("samsung", "8kg"),
        microwave("panasonic", 5),
        refrigerator("LG", 4)
    ]

    for device in appliances:
        device.turn_on()
        print("-" * 50)
