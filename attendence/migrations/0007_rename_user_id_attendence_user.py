# Generated by Django 3.2.5 on 2021-08-02 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0006_alter_attendence_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='user_id',
            new_name='user',
        ),
    ]