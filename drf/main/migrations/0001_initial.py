# Generated by Django 3.2.6 on 2021-12-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('id_card', models.CharField(max_length=255)),
            ],
        ),
    ]
