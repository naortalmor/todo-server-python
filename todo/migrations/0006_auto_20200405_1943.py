# Generated by Django 3.0.4 on 2020-04-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20200405_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(),
        ),
    ]
