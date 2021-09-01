# Generated by Django 3.2.5 on 2021-08-04 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pregunta', '0004_auto_20210804_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntasOpcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('preguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo', to='pregunta.preguntaunica')),
            ],
        ),
        migrations.CreateModel(
            name='CargarP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo', to='pregunta.pais')),
            ],
        ),
    ]
