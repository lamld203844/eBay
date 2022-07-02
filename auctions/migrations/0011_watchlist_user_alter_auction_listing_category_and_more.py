# Generated by Django 4.0.4 on 2022-07-02 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_rename_comments_comment_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='watchlist', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='category',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='photo',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
