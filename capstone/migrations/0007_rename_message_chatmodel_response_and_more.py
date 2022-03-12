# Generated by Django 4.0 on 2022-03-08 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0006_alter_groupdetails_user1_alter_groupdetails_user2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmodel',
            old_name='message',
            new_name='response',
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='description',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='model',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='theme',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
