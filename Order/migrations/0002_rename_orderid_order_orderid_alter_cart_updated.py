# Generated by Django 4.1.1 on 2023-01-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Order", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order", old_name="OrderId", new_name="orderId",
        ),
        migrations.AlterField(
            model_name="cart",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
