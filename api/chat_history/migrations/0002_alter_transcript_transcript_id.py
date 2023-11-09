# Generated by Django 4.0.1 on 2023-11-09 15:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat_history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='transcript_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
