# Generated by Django 5.0.6 on 2024-05-29 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auction_listing_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category',
            new_name='categoryName',
        ),
    ]