# Generated by Django 2.1.2 on 2018-10-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_auto_20181024_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(max_length=40),
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
    ]
