from models.vehicle import Vehicle
from models.garage import Garage

def main():

    garage = Garage()

    asx = Vehicle(
        vehicle_id=1,
        brand="Mitsubishi",
        model="ASX",
        version="HPE",
        year=2019,
        engine="2.0L 16V I4",
        transmission="AT CVT",
        fuel_type="Flex",
        mileage=98780
    )

    peugeot_207 = Vehicle(
        vehicle_id=2,
        brand="Peugeot",
        model="207",
        version="XR Hatchback",
        year=2012,
        engine="1.4L 8V I4",
        transmission="MT 5",
        fuel_type="Flex",
        mileage=114556,
    )

    garage.add_vehicle(asx)
    garage.add_vehicle(peugeot_207)

    found_vehicle = garage.find_vehicle(1)


    if found_vehicle:
        print("Veículo encontrado: \n")
        print(found_vehicle)
    else:
        print("Veículo não encontrado.")

    removed = garage.remove_vehicle(1)

    print(f"Veículo removido: {removed} \n")

    print("Veículos listados: \n")
    
    garage.list_vehicles()

if __name__ == "__main__":
    main()
