# Generated by Django 4.1.5 on 2023-02-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolwork', '0003_alter_student_classname'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rf_code',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, unique=True),
        ),
    ]