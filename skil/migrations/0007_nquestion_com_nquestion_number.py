# Generated by Django 4.1.2 on 2022-11-03 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skil', '0006_equestion_number_alter_equestion_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='nquestion',
            name='com',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nquestion',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
