# Generated by Django 4.0.4 on 2022-05-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender_jobs', '0003_alter_senderjobs_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrierjobs',
            name='arrival_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='carrierjobs',
            name='departure_date',
            field=models.DateField(),
        ),
    ]
