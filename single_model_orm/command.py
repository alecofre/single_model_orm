# Importar el modelo de Users
from users_app.models import *
Users.objects.all()

# Crear 3 nuevos Users
Users.objects.create(first_name="Esteban", last_name = "Dido", email_address = "estaban.dido@email.com", age = 33)
Users.objects.create(first_name="Elba", last_name = "Lazo", email_address = "elba.lazo@email.com", age = 27)
Users.objects.create(first_name="Armando", last_name = "Meza", email_address = "armando.meza@email.com", age = 55)

# Consulta recuperar todos los usuarios
Users.objects.all()

#Consulta recuperar el ultimo usuario
Users.objects.last()

# Consulta recuperar el primer usuario
Users.objects.first()

# Consulta: Cambie el usuario con id = 3 para que su apellido sea Pancakes.
user_update = Users.objects.get(id=3)
user_update.last_name = "Pancakes"
user_update.save()

# Consulta: Eliminar el usuario con id = 2 de la base de datos
user_delete = Users.objects.get(id=2)
user_delete.delete()

# Consulta: Obtenga todos los usuarios, ordenados por su nombre
Users.objects.all().order_by('first_name')

# BONUS Query: obtén todos los usuarios, ordenados por su nombre en orden descendente
Users.objects.all().order_by('-first_name')

