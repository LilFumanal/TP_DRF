# Generated by Django 5.0 on 2024-01-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiveManagement', '0002_rename_nom_beeyards_name_intervention'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='date',
            field=models.DateField(default='2002-03-20'),
            preserve_default=False,
        ),
    ]