from models.vehicle import Vehicle
from models.garage import Garage

MENU_WIDTH = 25

class CLI:
    def __init__(self, garage):
        self.garage = garage

    
    def show_menu(self):
        print("=========================")
        print("     GARAGE MANAGER")
        print("=========================")
        print("1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Buscar veículo")
        print("4 - Atualizar veículo")
        print("5 - Remover veículo")
        print("0 - Sair")

    def create_vehicle(self):
        vehicle_id = int(input("ID do veículo: "))
        brand = input("Marca: ")
        model = input("Modelo: ")
        version = input("Versão: ")
        year = input("Ano: ")
        engine = input("Motor: ")
        transmission = input("Transmissão: ")
        fuel_type = input("Combustível: ")
        mileage = int(input("Quilometragem: "))

        vehicle = Vehicle(
            vehicle_id,
            brand,
            model,
            version,
            year,
            engine,
            transmission,
            fuel_type,
            mileage
        )

        self.garage.add_vehicle(vehicle)
    

        print("Veículo cadastrado com sucesso!")

    def find_vehicle(self, vehicle_id):
        for vehicle in self.garage.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
            return None
        

    def run(self):
        while True:
            self.show_menu()
        
            option = input("\nEscolha uma opção: ")

            if option == "1":
                print("Cadastrar veículo")
                self.create_vehicle()

            elif option == "2":
                print("Listar veículos")
                self.garage.list_vehicles()

            elif option == "3":
                print("Buscar veículo")
                vehicle_id = int(input("Digite o ID do veículo desejado: "))
                vehicle = self.find_vehicle(vehicle_id)
                if vehicle:
                    print("=" * MENU_WIDTH)
                    print("Veículo encontrado")
                    print("=" * MENU_WIDTH)
                    print(vehicle)
                else:
                    print("Veículo não encontrado.")


            elif option == "0":
                print("Encerrando Garage Manager...")
                break

            else:
                print("Opção inválida")
