# Generated by Django 4.1 on 2022-09-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100, unique=True)),
                ('Created_By', models.CharField(default='Admin', max_length=25)),
                ('Added_date', models.CharField(default='dd-mm-yyyy', max_length=20)),
                ('Views', models.IntegerField(default='00')),
                ('Short_Text', models.TextField()),
            ],
        ),
    ]