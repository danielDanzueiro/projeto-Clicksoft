# Generated by Django 2.2.6 on 2019-10-26 00:11

from django.db import migracoes, modelos


class Migracao(migracoes.Migracao):

    initial = True

    dependencies = [
    ]

    operations = [
        migracoes.CreateModel(
            name='Nota',
            fields=[
                ('id', modelos.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', modelos.TextField(max_length=500)),
            ],
        ),
    ]
