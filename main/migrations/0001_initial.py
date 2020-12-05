# Generated by Django 3.0.5 on 2020-12-04 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('tags', models.CharField(default='', max_length=70)),
                ('open_for_f', models.CharField(max_length=7)),
                ('open_for_t', models.CharField(max_length=7)),
                ('quarantine', models.CharField(max_length=7)),
            ],
        ),
    ]
