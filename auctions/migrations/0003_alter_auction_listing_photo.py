# Generated by Django 4.0.4 on 2022-06-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_auction_listing_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='photo',
            field=models.URLField(blank=True),
        ),
    ]
