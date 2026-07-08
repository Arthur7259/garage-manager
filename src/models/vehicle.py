class Vehicle:
    def __init__(
            self,
            brand,
            model,
            version,
            year,
            engine,
            transmission,
            fuel_type,
            mileage,
    ):
        self.brand = brand
        self.model = model
        self.version = version
        self.year = year
        self.engine = engine
        self.transmission = transmission
        self.fuel_type = fuel_type
        self.mileage = mileage
    
    def __str__(self):
        return (
            f"{self.brand} {self.model} {self.version} {self.year}\n"
            f"Motor: {self.engine}\n"
            f"Transmissão: {self.transmission}\n"
            f"Combustível: {self.fuel_type}\n"
            f"Quilometragem: {self.mileage} km\n"
        ) 