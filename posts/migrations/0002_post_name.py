# Generated by Django 4.1.1 on 2022-10-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=140, verbose_name='Name'),
        ),
    ]