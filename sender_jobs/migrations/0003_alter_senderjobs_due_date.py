# Generated by Django 4.0.4 on 2022-05-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender_jobs', '0002_carrierjobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senderjobs',
            name='due_date',
            field=models.DateField(),
        ),
    ]
