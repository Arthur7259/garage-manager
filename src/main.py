from models.garage import Garage
from menus.cli import CLI



def main():

    garage = Garage()

    cli = CLI(garage)

    cli.run()

if __name__ == "__main__":
    main()