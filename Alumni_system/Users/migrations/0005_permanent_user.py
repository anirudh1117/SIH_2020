# Generated by Django 3.0.2 on 2020-01-20 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20200120_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permanent_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('college_name', models.CharField(max_length=50)),
                ('graduation_yr', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)])),
                ('roll_no', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=60)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]