# Generated by Django 5.0.2 on 2024-07-10 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_category_slug_remove_book_categories_book_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
