# Generated by Django 3.1.3 on 2021-02-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_auto_20210124_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='paymode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('No Money Collected', 'No Money Collected')], max_length=25, verbose_name='Payment Mode'),
        ),
    ]
