# Generated by Django 5.0.6 on 2024-07-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("outlet", "0013_rename_item_age_item_item_age_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="best_seller",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="eco_friendly",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="item",
            name="new_arrival",
            field=models.BooleanField(default=False),
        ),
    ]
