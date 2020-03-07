# Generated by Django 3.0.3 on 2020-03-05 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('splitbackend', '0002_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tab',
            name='owner_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='splitbackend.Profile'),
            preserve_default=False,
        ),
    ]
