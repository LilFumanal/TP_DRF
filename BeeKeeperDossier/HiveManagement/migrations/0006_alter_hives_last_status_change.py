# Generated by Django 5.0 on 2024-01-14 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiveManagement', '0005_alter_intervention_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hives',
            name='last_status_change',
            field=models.DateField(auto_now_add=True),
        ),
    ]
