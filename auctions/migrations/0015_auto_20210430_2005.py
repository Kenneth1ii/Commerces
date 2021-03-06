# Generated by Django 3.1.6 on 2021-04-30 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20210430_0427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionbids',
            name='currentbiduserid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userbought',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userlist',
        ),
        migrations.RemoveField(
            model_name='user',
            name='usersold',
        ),
        migrations.AddField(
            model_name='auctionbids',
            name='currentuserbid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currentuserbid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctionowner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='userbought',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctionbought', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='usersold',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctionsold', to=settings.AUTH_USER_MODEL),
        ),
    ]
