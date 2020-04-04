# Generated by Django 3.0.4 on 2020-03-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('is_done', models.BooleanField(default=False)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
