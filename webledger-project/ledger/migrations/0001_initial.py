# Generated by Django 3.1.3 on 2021-01-20 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collected_by',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Money Collected By',
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('mob_num', models.IntegerField(blank=True, null=True, unique=True)),
                ('address', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ViewDealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer', models.ManyToManyField(related_name='dealer', to='ledger.Dealer')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Dealer Permission Area',
            },
        ),
        migrations.CreateModel(
            name='RoadExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fooding', models.PositiveIntegerField(blank=True, default=0)),
                ('fuel', models.PositiveIntegerField(blank=True, default=0)),
                ('misc', models.TextField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('particulars', models.CharField(blank=True, max_length=100, verbose_name='Particulars')),
                ('debit', models.PositiveIntegerField(blank=True, default=0, verbose_name='Debit')),
                ('credit', models.PositiveIntegerField(blank=True, default=0, verbose_name='Credit')),
                ('paymode', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque')], max_length=10, verbose_name='Payment Mode')),
                ('new_balance', models.IntegerField(editable=False)),
                ('dr_cr', models.CharField(default='ab', editable=False, max_length=2, verbose_name='Dr/Cr')),
                ('invoice', models.ImageField(blank=True, upload_to=None, verbose_name='Invoice')),
                ('balance', models.IntegerField(default=0, editable=False)),
                ('dealer_ledger_number', models.IntegerField(default=0, editable=False)),
                ('collect_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ledger.collected_by', verbose_name='Collected By')),
                ('dealer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ledger.dealer', verbose_name='Dealer')),
            ],
        ),
        migrations.CreateModel(
            name='BrandNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('ledger_number', models.IntegerField(default=0)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.dealer')),
            ],
        ),
    ]
