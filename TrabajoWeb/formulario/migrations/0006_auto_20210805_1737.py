# Generated by Django 3.2.5 on 2021-08-05 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0005_ofertas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='vacante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo', to='formulario.ofertas'),
        ),
        migrations.AlterField(
            model_name='ofertas',
            name='imagan',
            field=models.ImageField(upload_to='formulario'),
        ),
    ]
