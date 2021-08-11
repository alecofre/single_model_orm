from django.db import models

# Create your models here.
class Users(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email_address = models.CharField(max_length=255)
     age = models.IntegerField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     # def __repr__(self):
     #      return f"Nombre: {self.first_name}, Apellido: {self.last_name}, Email: {self.email_address}, Edad: {self.age}"
     def __repr__(self):
          return f"Nombre: {self.first_name}, Apellido: {self.last_name}, Correo: {self.email_address}, Edad: {self.age}"

     def __str__(self):
          return f"Nombre: {self.first_name + self.last_name}"

