# Generated by Django 3.2.9 on 2021-11-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('comments', models.TextField(blank=True)),
                ('filename', models.FileField(upload_to='')),
            ],
        ),
    ]