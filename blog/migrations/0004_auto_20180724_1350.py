# Generated by Django 2.0.7 on 2018-07-24 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='upadated_at',
            new_name='updated_at',
        ),
    ]