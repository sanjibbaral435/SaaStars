# Generated by Django 2.0.3 on 2018-04-03 05:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20180403_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key_entity',
            name='key_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
