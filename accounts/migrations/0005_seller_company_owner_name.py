# Generated by Django 4.1.1 on 2022-10-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_comapny_address_seller_company_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='company_owner_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
