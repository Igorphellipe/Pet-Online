# Generated by Django 4.2.11 on 2024-04-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_alter_reserva_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='tamanho',
            field=models.IntegerField(choices=[(0, 'Pequeno'), (1, 'Médio'), (2, 'Grande')], verbose_name='Tamanho'),
        ),
    ]