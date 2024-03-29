# Generated by Django 3.0.dev20190528134031 on 2019-06-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('source', '0003_auto_20190618_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('body_text', models.TextField(null=True)),
                ('sources', models.ManyToManyField(to='source.Sources')),
            ],
        ),
    ]
