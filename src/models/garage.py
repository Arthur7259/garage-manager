from models.vehicle import Vehicle

class Garage:
    def __init__(self, vehicles=None, storage=None):
        self.storage = storage
        
        if vehicles is None:
            self.vehicles = []
        else:
            self.vehicles = vehicles

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
        else:
            print("Objeto inváqlido. Aqpenas veículos podem ser adicionados.")
        if self.storage:
            self.storage.save(self.vehicles)

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)
            print("-" * 50)

    def find_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
            
            return None
        
    def remove_vehicle(self, vehicle_id):
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle:
            self.vehicles.remove(vehicle)
        if self.storage:
            self.storage.save(self.vehicles)
            return True
        
        
        return False
    
    def update_vehicle(self, vehicle_id, **updates):
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle:
            for attribute, value in updates.items():
                if hasattr(vehicle, attribute):
                    setattr(vehicle, attribute, value)
                else:
                    print(f"Atributo inválido: {attribute}")
                if self.storage:
                    self.storage.save(self.vehicles)

            return True
        
        return False