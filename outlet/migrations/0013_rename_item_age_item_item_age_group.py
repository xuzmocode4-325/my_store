# Generated by Django 5.0.6 on 2024-07-13 16:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("outlet", "0012_alter_item_item_age_alter_item_item_gender"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="item_age",
            new_name="item_age_group",
        ),
    ]
