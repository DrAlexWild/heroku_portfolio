# Generated by Django 4.0.4 on 2022-05-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_projetc_topic_project_project_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='descricao',
            field=models.TextField(max_length=2000),
        ),
    ]