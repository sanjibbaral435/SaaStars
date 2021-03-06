# Generated by Django 2.0.3 on 2018-04-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20180403_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article_entity',
            name='author_fk',
        ),
        migrations.AddField(
            model_name='article_entity',
            name='author_fk',
            field=models.ManyToManyField(to='webapp.author_entity'),
        ),
        migrations.RemoveField(
            model_name='article_entity',
            name='key_fk',
        ),
        migrations.AddField(
            model_name='article_entity',
            name='key_fk',
            field=models.ManyToManyField(to='webapp.key_entity'),
        ),
    ]
