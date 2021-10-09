# Generated by Django 3.1.7 on 2021-09-05 11:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comlaint',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('mobilenum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=20)),
                ('mobilenum', models.IntegerField()),
                ('roomnumber', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.staffprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('mobile_num', models.IntegerField()),
                ('in_time', models.TimeField(auto_now_add=True)),
                ('out_time', models.TimeField(null=True)),
                ('visiting_to', models.ManyToManyField(to='students.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Replie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.staffprofile')),
                ('replying_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.comlaint')),
            ],
        ),
        migrations.AddField(
            model_name='comlaint',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentprofile'),
        ),
    ]
