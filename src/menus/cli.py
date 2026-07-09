from models.vehicle import Vehicle
from models.garage import Garage
from utils.input_helper import (read_year, read_int, read_non_empty, read_positive_int)

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
        brand = read_non_empty("Marca: ")
        model = read_non_empty("Modelo: ")
        version = read_non_empty("Versão: ")
        year = read_year("Ano: ")
        engine = read_non_empty("Motor: ")
        transmission = read_non_empty("Transmissão: ")
        fuel_type = read_non_empty("Combustível: ")
        mileage = read_positive_int("Quilometragem ")

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

    def search_by_id(self):
        vehicle_id = read_int("Digite o ID de veículo desejado: ")

        vehicle = self.garage.find_vehicle(vehicle_id)

        if vehicle:
            print("=" * MENU_WIDTH)
            print("Veículo encontrado")
            print("=" * MENU_WIDTH)
            print(vehicle)
        else:
            print("Veículo não encontrado")

    def search_by_brand(self):
        brand = read_non_empty("Digite a marca do veículo: ")

        vehicles = self.garage.search_by_brand(brand)

        if vehicles:
            print("=" * MENU_WIDTH)
            print("Veículos encontrados")
            print("=" * MENU_WIDTH)

            for vehicle in vehicles:
                print(vehicle)
                print("=" * MENU_WIDTH)
        else:
            print("Nenhum veículo encontrado.")

    def search_by_model(self):
        model = read_non_empty("Digite o modelo do veículo: ")

        vehicles = self.garage.search_by_model(model)

        if vehicles:
            print("=" * MENU_WIDTH)
            print("Veículos encontrados")
            print("=" * MENU_WIDTH)

            for vehicle in vehicles:
                print(vehicle)
                print("=" * MENU_WIDTH)
        
        else:
            print("Nenhum veículo encontrado.")

    def search_by_fuel_type(self):
        fuel_type = read_non_empty("Digite o tipo de combustível do veículo: ")

        vehicles = self.garage.search_by_fuel_type(fuel_type)

        if vehicles:
            print("=" * MENU_WIDTH)
            print("Veículos encontrados")
            print("=" * MENU_WIDTH)

            for vehicle in vehicles:
                print(vehicle)
                print("=" * MENU_WIDTH)
        
        else:
            print("Nenhum veículo encontrado.")


    def search_menu(self):
        while True:
            print("=" * MENU_WIDTH)
            print("Buscar veículo")
            print("=" * MENU_WIDTH)

            print("1 - Buscar por ID")
            print("2 - Buscar por marca")
            print("3 - Buscar por modelo")
            print("4 - Buscar por tipo de combustível")
            print("0 - Voltar")

            option = input("\nEscolha uma opção de busca: ")

            if option == "1":
                self.search_by_id()
            
            elif option == "2":
                self.search_by_brand()

            elif option == "3":
                self.search_by_model()
            
            elif option == "0":
                break

            else:
                print("Opção inválida")


    def find_vehicle(self, vehicle_id):
        for vehicle in self.garage.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
            return None
        
    def update_vehicle(self):
        print("=" * MENU_WIDTH)
        print("Atualizar veículo")
        print("=" * MENU_WIDTH)

        vehicle_id = read_positive_int("ID do veículo: ")

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
            new_value = read_year("Ano atualizado: ")
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
            new_value = read_positive_int("Quilometragem atualizada: ")
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
                self.search_menu()

            
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
