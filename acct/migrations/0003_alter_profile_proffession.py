# Generated by Django 4.1.3 on 2022-12-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acct', '0002_remove_profile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='proffession',
            field=models.CharField(default='Member', max_length=50),
        ),
    ]
