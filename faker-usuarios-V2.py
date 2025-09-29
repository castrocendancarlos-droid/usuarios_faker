from faker import Faker

# Crear instancia de Faker
fake = Faker('es_ES')  # Pode cambiarse a outro idioma se prefires

usuarios = {}

for codigo in range(1, 16):
    usuarios[codigo] = {
        'nome': fake.name(),
        'direccion': fake.address().replace("\n", ", "),
        'correo_electronico': fake.email(),
        'telefono': fake.phone_number()
    }

# Mostrar resultado
for codigo, datos in usuarios.items():
    print(f"Código {codigo}: {datos}")