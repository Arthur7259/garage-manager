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

    onix = Vehicle(
        vehicle_id=3,
        brand="Chevrolet",
        model="Onix",
        version="Lt Hatchback",
        year=2016,
        engine="1.0L 8V I4",
        transmission="MT 5",
        fuel_type="Flex",
        mileage=112882,
    )


    garage.add_vehicle(asx)
    garage.add_vehicle(peugeot_207)
    garage.add_vehicle(onix)

    found_vehicle = garage.find_vehicle(1)

    if found_vehicle:
        print("Veículo encontrado: \n")
        print(found_vehicle)
    else:
        print("Veículo não encontrado.")

    removed = garage.remove_vehicle(2)

    print("Veículo removido: \n", removed)


    updated = garage.update_vehicle(
        1,
        mileage=103453,
    )

    print("Atualização: \n", updated)

    print("Veículos listados: \n")

    garage.list_vehicles()

if __name__ == "__main__":
    main()
