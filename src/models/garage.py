from models.vehicle import Vehicle

class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
        else:
            print("Objeto inváqlido. Aqpenas veículos podem ser adicionados.")

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
            return True

        return False