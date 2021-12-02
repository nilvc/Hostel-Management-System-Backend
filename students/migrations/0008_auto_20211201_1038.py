# Generated by Django 3.1.7 on 2021-12-01 05:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('staff_members', '0004_delete_replie'),
        ('students', '0007_auto_20211130_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comlaint',
            name='status',
        ),
        migrations.CreateModel(
            name='Replie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='staff_members.staffprofile')),
                ('replying_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.comlaint')),
            ],
        ),
    ]