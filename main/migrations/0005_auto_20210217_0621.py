# Generated by Django 3.1.6 on 2021-02-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_date_int'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_int',
            field=models.IntegerField(null=True),
        ),
    ]
