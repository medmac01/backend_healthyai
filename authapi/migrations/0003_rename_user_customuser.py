# Generated by Django 4.1.7 on 2023-03-01 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authapi", "0002_alter_user_email"),
    ]

    operations = [
        migrations.RenameModel(old_name="User", new_name="CustomUser",),
    ]
