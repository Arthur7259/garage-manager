import json
from pathlib import Path

from models.vehicle import Vehicle

class JsonStorage:

    def __init__(self):
        self.file_path = Path(__file__).parent.parent.parent / "data" / "vehicles.json"

    def save(self, vehicles):
        data = []
        for vehicle in vehicles:
            vehicle.to_dict()
            data.append(vehicle.to_dict())
        
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )
    def load(self):
        if not self.file_path.exists():
            return[]
        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        
        vehicles = []

        for item in data:
            vehicles.append(Vehicle.from_dict(item))
        
        return vehicles