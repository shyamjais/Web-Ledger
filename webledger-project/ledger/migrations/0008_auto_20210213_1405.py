# Generated by Django 3.1.3 on 2021-02-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0007_auto_20210206_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewdealer',
            name='dealer',
            field=models.ManyToManyField(blank=True, related_name='dealer', to='ledger.Dealer'),
        ),
    ]
