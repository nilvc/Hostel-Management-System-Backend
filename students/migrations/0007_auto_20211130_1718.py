# Generated by Django 3.1.7 on 2021-11-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_comlaint_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='profile_pic',
            field=models.FileField(default=None, upload_to='D:\\Django-Projects\\Hostel-management-system-Backend\\media'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
