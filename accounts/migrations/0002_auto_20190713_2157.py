# Generated by Django 3.0.dev20190528134031 on 2019-07-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password1',
            field=models.CharField(max_length=100, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
