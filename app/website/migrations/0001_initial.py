# Generated by Django 3.1.1 on 2020-09-19 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('vat_prefix', models.CharField(default='ATU', max_length=7)),
                ('vat', models.CharField(max_length=31)),
                ('city', models.CharField(max_length=31)),
                ('phone', models.CharField(max_length=31)),
                ('street', models.CharField(max_length=63)),
                ('plz', models.PositiveIntegerField()),
                ('present', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Kunde',
                'verbose_name_plural': 'Kunden',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('surname', models.CharField(max_length=264)),
                ('born_on', models.DateField()),
                ('ssn', models.CharField(max_length=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('nationality', models.CharField(max_length=264)),
            ],
            options={
                'verbose_name': 'Mitarbeiterinnen',
                'verbose_name_plural': 'Mitarbeiter',
            },
        ),
        migrations.CreateModel(
            name='ProjectManagerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('title', models.CharField(max_length=7)),
                ('present', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Projektleiterinnen',
                'verbose_name_plural': 'Projektleitern',
            },
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=31)),
                ('project_id', models.CharField(blank=True, max_length=255, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.customermodel')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.projectmanagermodel')),
            ],
            options={
                'verbose_name': 'Baustelle',
                'verbose_name_plural': 'Baustellen',
            },
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField()),
                ('price', models.FloatField()),
                ('currency', models.CharField(default='EUR', max_length=7)),
                ('name', models.CharField(max_length=1023)),
                ('unit', models.PositiveSmallIntegerField(choices=[(0, 'Stk.'), (1, 'PA'), (2, 'lfm'), (3, 'm²'), (4, 'Std.')])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.projectmodel')),
            ],
            options={
                'verbose_name': 'Leistung',
                'verbose_name_plural': 'Leistungen',
            },
        ),
    ]
