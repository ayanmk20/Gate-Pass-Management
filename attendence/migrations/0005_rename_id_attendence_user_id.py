# Generated by Django 3.2.5 on 2021-08-02 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0004_rename_userid_attendence_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='id',
            new_name='user_id',
        ),
    ]