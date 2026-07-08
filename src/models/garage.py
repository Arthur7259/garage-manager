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

    