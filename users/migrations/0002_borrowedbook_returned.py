# Generated by Django 5.0.2 on 2024-07-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowedbook',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
