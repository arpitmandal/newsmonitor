# Generated by Django 3.0.dev20190528134031 on 2019-07-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190713_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='password1',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
