# Generated by Django 3.0.3 on 2020-03-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitbackend', '0007_auto_20200305_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=17),
        ),
        migrations.AlterField(
            model_name='tab',
            name='title',
            field=models.CharField(default='Outing', max_length=30),
        ),
    ]
