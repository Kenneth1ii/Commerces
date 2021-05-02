# Generated by Django 3.1.6 on 2021-04-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20210427_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='watch',
        ),
        migrations.AlterField(
            model_name='user',
            name='userwatchlist',
            field=models.ManyToManyField(blank=True, related_name='userwatch', to='auctions.AuctionListing'),
        ),
        migrations.DeleteModel(
            name='AuctionWatch',
        ),
    ]