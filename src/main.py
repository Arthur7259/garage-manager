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

    cli = CLI(garage)
    cli.run()

if __name__ == "__main__":
    main()

