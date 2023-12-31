# Generated by Django 4.2.3 on 2023-08-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_contato_options_contato_lido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Envio'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.TextField(verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
