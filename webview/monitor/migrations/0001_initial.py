# Generated by Django 2.2.6 on 2019-10-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angle', models.FloatField()),
                ('distance', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
