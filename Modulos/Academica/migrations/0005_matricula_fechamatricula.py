# Generated by Django 3.1.3 on 2022-11-02 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0004_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='fechaMatricula',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
