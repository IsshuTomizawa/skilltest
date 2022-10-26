# Generated by Django 4.1.2 on 2022-10-26 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('sele1', models.TextField()),
                ('sele2', models.TextField()),
                ('sele3', models.TextField()),
                ('answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Percent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField()),
                ('true', models.IntegerField(default=0)),
                ('false', models.IntegerField(default=0)),
            ],
        ),
    ]