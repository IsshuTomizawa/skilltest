# Generated by Django 4.1.2 on 2022-11-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skil', '0007_nquestion_com_nquestion_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equestion',
            name='answer',
            field=models.CharField(max_length=1),
        ),
    ]
