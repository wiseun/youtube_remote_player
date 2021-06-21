# Generated by Django 3.2.4 on 2021-06-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemotePlayerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPlaying', models.BooleanField(default=False)),
                ('currentLink', models.CharField(max_length=200)),
                ('playList', models.TextField()),
            ],
        ),
    ]
