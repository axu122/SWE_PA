# Generated by Django 3.0.4 on 2020-05-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer_assessment', '0012_auto_20200501_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='sent_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='54748293', max_length=100),
        ),
    ]
