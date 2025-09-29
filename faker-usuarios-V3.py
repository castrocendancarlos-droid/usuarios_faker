from faker import Faker
import random

fake = Faker('es_ES')

usuarios = {}
nomes_usados = set()  # Para gardar os nomes xa xerados

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

# Selecciona a un usuario ao chou, e mostra por pantalla a mensaxe indicada
# empregamos o modulo random
# Seleccionar aleatoriamente un ID de usuario
id_chou = random.choice(list(usuarios.keys()))

# Danos o nome do usuario que sae agraciado
agraciado = usuarios[id_chou]['nome']

# Mostrar mensaje
print(f'\n O usuario chamado {agraciado} foi o afortunado')