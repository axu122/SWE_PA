# Generated by Django 3.0.4 on 2020-04-21 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer_assessment', '0004_auto_20200420_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='year',
            field=models.CharField(default='2020', max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='76417655', max_length=100),
        ),
    ]
