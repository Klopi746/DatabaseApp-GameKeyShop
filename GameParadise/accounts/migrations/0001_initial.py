# Generated by Django 3.2.16 on 2024-11-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(default='Vasya@gmail.cat', max_length=40)),
                ('password', models.CharField(default='1234', max_length=40)),
            ],
        ),
    ]
