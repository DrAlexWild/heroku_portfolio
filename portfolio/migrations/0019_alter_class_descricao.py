# Generated by Django 4.0.4 on 2022-05-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_alter_language_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='descricao',
            field=models.TextField(max_length=2000),
        ),
    ]
