from django.db import modelos

# Create your models here.

class Nota(modelos.Model):
    texto = modelos.TextField(max_length=500)