# Generated by Django 4.2.4 on 2023-08-31 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0002_alter_auctionlisting_category_alter_bid_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlisting",
            name="date",
            field=models.DateField(null=True),
        ),
    ]
