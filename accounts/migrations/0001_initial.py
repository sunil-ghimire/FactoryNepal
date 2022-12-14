# Generated by Django 4.1.1 on 2022-11-20 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('full_name', models.CharField(max_length=100)),
                ('password2', models.CharField(blank=True, max_length=100)),
                ('user_type', models.CharField(choices=[('user', 'User'), ('seller', 'Seller')], default='user', max_length=6)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=100)),
                ('company_owner_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=200)),
                ('company_phone', models.CharField(max_length=20)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('linkedin', models.CharField(blank=True, max_length=100)),
                ('youtube', models.CharField(blank=True, max_length=100)),
                ('number_of_employee', models.CharField(blank=True, max_length=100)),
                ('company_type', models.CharField(blank=True, max_length=100)),
                ('company_size', models.CharField(blank=True, max_length=100)),
                ('company_description', models.TextField(blank=True)),
                ('company_logo', models.ImageField(blank=True, upload_to='images/')),
                ('company_banner', models.ImageField(blank=True, upload_to='images/')),
                ('company_location', models.CharField(blank=True, max_length=100)),
                ('company_country', models.CharField(blank=True, max_length=100)),
                ('company_state', models.CharField(blank=True, max_length=100)),
                ('company_city', models.CharField(blank=True, max_length=100)),
                ('company_zip', models.CharField(blank=True, max_length=100)),
                ('company_latitude', models.CharField(blank=True, max_length=100)),
                ('company_longitude', models.CharField(blank=True, max_length=100)),
                ('company_established', models.CharField(blank=True, max_length=100)),
                ('company_pan_number', models.CharField(blank=True, max_length=100)),
                ('company_pan_document', models.ImageField(blank=True, upload_to='images/')),
                ('slug', models.SlugField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sellers',
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.productcategory')),
            ],
            options={
                'verbose_name_plural': 'Product Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('is_admin_approved', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.productcategory')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.productsubcategory')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.seller')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]