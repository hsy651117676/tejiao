# Generated by Django 3.2.7 on 2022-01-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schooltype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rowid', models.IntegerField(null=True)),
                ('schooltype', models.CharField(max_length=30, null=True)),
                ('code', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]