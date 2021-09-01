# Generated by Django 3.2.5 on 2021-08-10 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worksample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('mensaje', models.TextField()),
                ('caso', models.TextField()),
                ('final_men', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pregunta_mol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opcional', to='work.preguntamotivacional')),
            ],
        ),
    ]
