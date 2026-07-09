from models.garage import Garage
from menus.cli import CLI
from storage.json_storage import JsonStorage
from models.vehicle import Vehicle



def main():

    storage = JsonStorage()

    vehicles = storage.load()

    garage = Garage(
        vehicles=vehicles,
        storage=storage
    )

    resultados = garage.search_by_brand("Peugeot")

    for vehicle in resultados:
        print(vehicle)

    cli = CLI(garage)
    cli.run()

if __name__ == "__main__":
    main()

