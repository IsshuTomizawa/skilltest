# Generated by Django 4.1.2 on 2022-11-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skil', '0013_remove_percent_ques'),
    ]

    operations = [
        migrations.AddField(
            model_name='percent',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
