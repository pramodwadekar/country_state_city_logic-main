# Generated by Django 4.2.6 on 2023-10-30 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.IntegerField()),
                ('country_name', models.CharField(max_length=50)),
                ('country_value', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('Email', models.EmailField(max_length=50)),
                ('Age', models.BigIntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Qualification', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.IntegerField()),
                ('state_name', models.CharField(max_length=50)),
                ('state_value', models.CharField(max_length=10)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField()),
                ('city_name', models.CharField(max_length=50)),
                ('city_value', models.CharField(max_length=10)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.state')),
            ],
        ),
    ]
