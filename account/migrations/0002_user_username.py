# Generated by Django 3.0 on 2020-04-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='Muniraj', max_length=255, verbose_name='username'),
        ),
    ]