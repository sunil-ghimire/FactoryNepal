# Generated by Django 4.1.1 on 2022-12-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='is_admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]
