# Generated by Django 5.0.6 on 2024-05-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_auction_listing_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]