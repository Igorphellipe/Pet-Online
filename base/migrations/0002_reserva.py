# Generated by Django 4.2.3 on 2023-08-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_pet', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=25)),
                ('dia_da_reserva', models.DateField(auto_now_add=True)),
                ('observacao', models.TextField()),
            ],
        ),
    ]
