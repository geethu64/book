# Generated by Django 4.0 on 2022-01-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
