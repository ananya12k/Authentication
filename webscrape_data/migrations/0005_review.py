# Generated by Django 4.1.13 on 2024-03-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrape_data', '0004_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('experience', models.TextField(default='Experience')),
                ('photos', models.ImageField(upload_to='images/')),
                ('rating', models.FloatField()),
            ],
        ),
    ]
