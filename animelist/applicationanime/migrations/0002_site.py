# Generated by Django 4.0.4 on 2022-05-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationanime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('url_site', models.CharField(max_length=100)),
            ],
        ),
    ]
