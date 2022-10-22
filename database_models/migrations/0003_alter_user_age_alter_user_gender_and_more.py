# Generated by Django 4.1 on 2022-10-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_models', '0002_alter_user_bio_alter_user_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='occupation',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
