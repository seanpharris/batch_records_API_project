# Generated by Django 3.2.9 on 2021-11-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batchjob',
            name='id',
        ),
        migrations.AlterField(
            model_name='batchjob',
            name='batch_number',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
