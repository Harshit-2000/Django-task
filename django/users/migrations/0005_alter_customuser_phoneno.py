# Generated by Django 4.0 on 2021-12-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_options_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phoneNo',
            field=models.CharField(max_length=12),
        ),
    ]