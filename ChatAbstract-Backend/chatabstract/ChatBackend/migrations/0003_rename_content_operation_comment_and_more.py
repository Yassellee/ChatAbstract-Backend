# Generated by Django 4.2 on 2023-05-14 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBackend', '0002_operation_rename_date_chat_datetime_alter_chat_gpt_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='content',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='operation',
            old_name='type',
            new_name='text',
        ),
    ]
