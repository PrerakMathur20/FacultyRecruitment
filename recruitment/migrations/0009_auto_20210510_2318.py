# Generated by Django 2.2.20 on 2021-05-10 17:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0008_auto_20210510_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 10, 17, 48, 32, 753313, tzinfo=utc)),
        ),
    ]
