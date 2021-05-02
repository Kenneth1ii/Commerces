# Generated by Django 3.1.6 on 2021-04-26 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210422_0338'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionWatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watching', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='auctionbids',
            old_name='CurrentBid',
            new_name='currentBid',
        ),
        migrations.AddField(
            model_name='user',
            name='usercommentlist',
            field=models.ManyToManyField(related_name='usercomment', to='auctions.AuctionComment'),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='watching',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctionwatch', to='auctions.auctionwatch'),
        ),
        migrations.AddField(
            model_name='user',
            name='userwatchlist',
            field=models.ManyToManyField(related_name='userwatch', to='auctions.AuctionWatch'),
        ),
    ]