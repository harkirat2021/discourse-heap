# Generated by Django 3.1.7 on 2021-03-16 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0005_auto_20210301_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='conclusion',
            new_name='state',
        ),
        migrations.AddField(
            model_name='profile',
            name='common_ground_points',
            field=models.IntegerField(default=0),
        ),
    ]
