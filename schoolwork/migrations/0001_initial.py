# Generated by Django 4.1.5 on 2023-02-07 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(choices=[('LKG', 'LKG'), ('UKG', 'UKG'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=200)),
                ('nationality', models.CharField(choices=[('INDIAN', 'INDIAN'), ('OTHER', 'OTHER')], max_length=200)),
                ('city', models.CharField(choices=[('PURNEA', 'PURNEA'), ('BHAGALPUR', 'BHAGALPUR')], max_length=30)),
                ('state', models.CharField(max_length=200)),
                ('pin_code', models.IntegerField()),
                ('contact', models.CharField(max_length=25)),
                ('image', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('dob', models.DateField()),
                ('className', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schoolwork.classes')),
            ],
        ),
    ]
