# Generated by Django 3.1.3 on 2022-11-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0002_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('docente', models.CharField(max_length=100)),
            ],
        ),
    ]
