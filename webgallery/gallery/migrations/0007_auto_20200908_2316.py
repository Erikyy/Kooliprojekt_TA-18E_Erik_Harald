# Generated by Django 3.1.1 on 2020-09-08 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20200908_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createpost',
            old_name='user',
            new_name='author',
        ),
    ]