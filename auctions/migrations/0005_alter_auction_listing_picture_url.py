# Generated by Django 5.0.6 on 2024-05-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_categories_auction_listing_buyer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='picture_url',
            field=models.CharField(blank=True, max_length=240),
        ),
    ]
