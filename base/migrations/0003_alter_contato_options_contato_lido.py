# Generated by Django 4.2.3 on 2023-08-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reserva'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-data'], 'verbose_name': 'Fomulário de Contato', 'verbose_name_plural': 'Fomulários de Contatos'},
        ),
        migrations.AddField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(blank=True, default=False, verbose_name='Lido'),
        ),
    ]
