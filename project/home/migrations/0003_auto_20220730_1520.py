# Generated by Django 3.1.1 on 2022-07-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220730_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_entry',
            name='old_house_no',
            field=models.CharField(max_length=30, verbose_name='Old House No.'),
        ),
    ]
