# Generated by Django 5.0.6 on 2024-05-29 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_rename_category_categories_categoryname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_listing',
            name='item_category',
        ),
        migrations.AddField(
            model_name='auction_listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.categories'),
        ),
    ]