# Generated by Django 2.1.7 on 2019-02-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hjres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
