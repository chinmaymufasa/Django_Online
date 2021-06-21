# Generated by Django 3.2.4 on 2021-06-21 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210621_0333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='auction_id',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='auction_id',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='auction_id',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Auction',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
