# Generated by Django 3.2.5 on 2021-08-02 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_college_rollno'),
        ('attendence', '0005_rename_id_attendence_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='college.college'),
        ),
    ]
