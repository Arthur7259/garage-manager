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
        vehicle_id = self.garage.generate_id()
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
    
        print(f"Veículo cadastrado com sucesso! ID: {vehicle_id}")

    def find_vehicle(self, vehicle_id):
        for vehicle in self.garage.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
            return None
        
    def update_vehicle(self):
        print("=" * MENU_WIDTH)
        print("Atualizar veículo")
        print("=" * MENU_WIDTH)

        vehicle_id = int(input("ID do veículo: "))

        vehicle = self.garage.find_vehicle(vehicle_id)

        if not vehicle:
            print("=" * MENU_WIDTH)
            print("Veículo não encontrado.")
            print("=" * MENU_WIDTH)
            return
        print("=" * MENU_WIDTH)
        print("Veículo encontrado!")
        print("=" * MENU_WIDTH)
        print(vehicle)

        print("\nO que deseja atualizar?")
        print("1 - Marca")
        print("2 - Modelo")
        print("3 - Versão")
        print("4 - Ano")
        print("5 - Motor")
        print("6 - Transmissão")
        print("7 - Combustível")
        print("8 - Quilometragem")
        print("0 - Cancelar")

        option = input("\nEscolha uma opção: ")

        if option == "1":
            new_value = input("Noca marca: ")
            self.garage.update_vehicle(vehicle_id, brand=new_value)
        
        elif option == "2":
            new_value = input("Novo modelo: ")
            self.garage.update_vehicle(vehicle_id, model=new_value)
        
        elif option == "3":
            new_value = input("Nova versão: ")
            self.garage.update_vehicle(vehicle_id, version=new_value)
        
        elif option == "4":
            new_value = int(input("Ano atualizado: "))
            self.garage.update_vehicle(vehicle_id, year=new_value)
        
        elif option == "5":
            new_value = input("Novo motor: ")
            self.garage.update_vehicle(vehicle_id, engine=new_value)
        
        elif option == "6":
            new_value = input("Nova transmissão: ")
            self.garage.update_vehicle(vehicle_id, transmission=new_value)
        
        elif option == "7":
            new_value = input("Novo combustível: ")
            self.garage.update_vehicle(vehicle_id, fuel_type=new_value)
        
        elif option == "8":
            new_value = int(input("Quilometragem atualizada: "))
            self.garage.update_vehicle(vehicle_id, mileage=new_value)
        
        elif option == "0":
            print("Atualização cancelada.")
            return
        
        else:
            print("Opção inválida.")
            return
        
        print("=" * MENU_WIDTH)
        print("Dados atualizados!")
        print("=" * MENU_WIDTH)
        print(vehicle)
    
    def remove_vehicle(self):
        print("=" * MENU_WIDTH)
        print("Remover veículo")
        print("=" * MENU_WIDTH)

        vehicle_id = int(input("ID do veículo: "))

        if self.garage.remove_vehicle(vehicle_id):
            print(f"Veículo {vehicle_id} removido com sucesso!")
        else:
            print("Veículo não encontrado.")
        

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
            
            elif option == "4":
                print("Atualizar veículo")
                self.update_vehicle()

            elif option == "5":
                print("Remover veículo")
                self.remove_vehicle()

            elif option == "0":
                print("Encerrando Garage Manager...")
                break

            else:
                print("Opção inválida")
