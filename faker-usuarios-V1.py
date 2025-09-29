from faker import Faker
import csv
from pprint import pprint

# Crear instancia de Faker en español
fake = Faker('es_ES')

# Diccionario para almacenar los usuarios
usuarios = {}

# Generar 15 usuarios
for i in range(1, 16):
    usuarios[i] = {
        "nome": fake.name(),
        "dirección": fake.street_address(),
        "correo electrónico": fake.email(),
        "teléfono": fake.phone_number()
    }

# Mostrar los usuarios por pantalla 
print("Usuarios generados:\n")
pprint(usuarios)
