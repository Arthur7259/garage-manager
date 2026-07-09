from datetime import datetime

FIRST_CAR_YEAR = 1886

def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Digite um número válido!")

def read_non_empty(message):
    while True:
        value = input(message).strip()

        if value:
            return value
        
        print("Este campo não pode ficar vazio.")

def read_positive_int(message):
    while True:
        value = read_int(message)

        if value >= 0:
            return value
        
        print("O valor deve ser maior ou igual a zero.")

def read_year(message):
    current_year = datetime.now().year

    while True:
        year = read_int(message)

        if year < FIRST_CAR_YEAR:
            print("Ano inválido para automóveis.")
            continue

        if year > current_year + 1:
            print("O ano informado ainda não é válido.")
            continue

        return year