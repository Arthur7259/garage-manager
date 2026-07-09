from models.vehicle import Vehicle

class Garage:
    def __init__(self, vehicles=None, storage=None):
        self.storage = storage

        if vehicles is None:
            self.vehicles = []
        else:
            self.vehicles = vehicles

    def generate_id(self):
        if not self.vehicles:
            return 1

        return max(vehicle.vehicle_id for vehicle in self.vehicles) + 1

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
        else:
            print("Objeto inválido. Aqpenas veículos podem ser adicionados.")
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
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:

                self.vehicles.remove(vehicle)

                if self.storage:
                    self.storage.save(self.vehicles)
                
                return True
            
        print("Não encontrei nenhum veículo")
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

    def search_by_brand(self, brand):
        results = []

        brand = brand.strip().lower()

        for vehicle in self.vehicles:
            if brand in vehicle.brand.lower():
                results.append(vehicle)
        
        return results
    
    def search_by_model(self, model):
        results = []

        model = model.strip().lower()

        for vehicle in self.vehicles:
            if model.lower() in vehicle.model.lower():
                results.append(vehicle)
        
        return results
    
    def search_by_fuel_type(self, fuel_type):
        results = []

        for vehicle in self.vehicles:
            if vehicle.fuel_type.lower() == fuel_type.lower():
                results.append(vehicle)

        return results