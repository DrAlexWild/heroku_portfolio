# Generated by Django 4.0.4 on 2022-05-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_blog_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
