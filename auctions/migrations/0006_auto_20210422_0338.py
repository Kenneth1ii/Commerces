# Generated by Django 3.1.6 on 2021-04-22 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210420_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctionbidding', to='auctions.auctionbids'),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctioncomment', to='auctions.auctioncomment'),
        ),
    ]
