# Generated by Django 3.1.7 on 2021-09-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visitors', '0002_auto_20210911_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='mobile_num',
            field=models.BigIntegerField(),
        ),
    ]