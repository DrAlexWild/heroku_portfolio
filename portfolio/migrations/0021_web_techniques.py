# Generated by Django 4.0.4 on 2022-06-02 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_news_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web_Techniques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=2000)),
                ('link', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
