# Generated by Django 3.2.16 on 2024-11-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='i_need_name', max_length=40)),
                ('genre', models.CharField(default='NoGenre', max_length=40)),
                ('price', models.IntegerField(default=100)),
                ('sold', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('description', models.TextField(default='This is a good game, I think...', max_length=400)),
            ],
        ),
    ]
