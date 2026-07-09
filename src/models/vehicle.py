class Vehicle:
    def __init__(
            self,
            vehicle_id,
            brand,
            model,
            version,
            year,
            engine,
            transmission,
            fuel_type,
            mileage,
    ):
        
        self.vehicle_id = vehicle_id
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
            f"ID: {self.vehicle_id}\n"
            f"{self.brand} {self.model} {self.version} - {self.year}\n"
            f"Motor: {self.engine}\n"
            f"Transmissão: {self.transmission}\n"
            f"Combustível: {self.fuel_type}\n"
            f"Quilometragem: {self.mileage} km\n"
        ) 
    
    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "brand": self.brand,
            "model": self.model,
            "version": self.version,
            "year": self.year,
            "engine": self.engine,
            "transmission": self.transmission,
            "fuel_type": self.fuel_type,
            "mileage": self.mileage,
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            vehicle_id=data["vehicle_id"],
            brand=data["brand"],
            model=data["model"],
            version=data["version"],
            year=data["year"],
            engine=data["engine"],
            transmission=data["transmission"],
            fuel_type=data["fuel_type"],
            mileage=data["mileage"]
        )