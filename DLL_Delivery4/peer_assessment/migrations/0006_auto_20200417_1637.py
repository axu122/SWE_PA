# Generated by Django 3.0.3 on 2020-04-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer_assessment', '0005_auto_20200417_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='67500292', max_length=100),
        ),
    ]
