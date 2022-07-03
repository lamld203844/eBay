# Generated by Django 4.0.4 on 2022-07-02 09:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_rename_user_watchlist_watcher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='watcher',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='watcher',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]