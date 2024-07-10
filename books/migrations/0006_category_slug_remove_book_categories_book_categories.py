# Generated by Django 5.0.2 on 2024-07-09 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.category'),
        ),
    ]
