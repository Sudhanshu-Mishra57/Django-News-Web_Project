# Generated by Django 4.1 on 2022-09-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_App', '0002_alter_news_added_date_alter_news_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Count',
            field=models.IntegerField(default='00'),
        ),
    ]