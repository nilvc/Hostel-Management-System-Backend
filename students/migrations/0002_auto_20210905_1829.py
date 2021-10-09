# Generated by Django 3.1.7 on 2021-09-05 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='comlaint',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='students.studentprofile'),
        ),
        migrations.AlterField(
            model_name='replie',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='students.staffprofile'),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='owner',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='owner',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]