# Generated by Django 3.0.3 on 2020-03-16 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('point_rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('account', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('name_kr', models.CharField(blank=True, max_length=50, null=True)),
                ('name_eng', models.CharField(blank=True, max_length=50, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('detailed_address', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('marketing_agree', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Gender')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Grade')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Job')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
