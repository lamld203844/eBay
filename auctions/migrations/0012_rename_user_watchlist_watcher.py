# Generated by Django 4.0.4 on 2022-07-02 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_watchlist_user_alter_auction_listing_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='user',
            new_name='watcher',
        ),
    ]
