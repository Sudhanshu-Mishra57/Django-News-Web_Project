# Generated by Django 4.1 on 2022-09-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.TextField()),
                ('Added_date', models.CharField(default='dd-mm-yyyy', max_length=20)),
            ],
        ),
    ]
