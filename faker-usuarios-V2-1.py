from faker import Faker

fake = Faker('es_ES')

usuarios = {}           #diccionario usuarios
nomes_usados = set()    # Para gardar os nomes xa xerados

codigo = 1
while codigo <= 15:
    nome = fake.name()
    
    # Comprobar se o nome xa foi usado
    if nome in nomes_usados:
        continue  # Saltar e xerar outro nome

    nomes_usados.add(nome)

    usuarios[codigo] = {
        'nome': nome,
        'direccion': fake.address().replace("\n", ", "),
        'correo_electronico': fake.email(),
        'telefono': fake.phone_number()
    }

    codigo += 1

# Mostrar resultado
for codigo, datos in usuarios.items():
    print(f"Código {codigo}: {datos}")