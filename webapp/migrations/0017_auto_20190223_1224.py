# Generated by Django 2.0.10 on 2019-02-23 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_useraccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]
