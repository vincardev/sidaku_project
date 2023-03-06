# Generated by Django 4.1 on 2022-12-09 05:00

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umkmdata', '0005_alter_umkmmodel_dtu_bypsnunit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BentukUsaha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('deskripsi', models.CharField(blank=True, default='', max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='nama', unique=True)),
            ],
            options={
                'verbose_name_plural': 'bentuk_usaha',
                'db_table': 'bentuk_usaha',
            },
        ),
        migrations.CreateModel(
            name='BidangUsaha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('deskripsi', models.CharField(blank=True, default='', max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='nama', unique=True)),
            ],
            options={
                'verbose_name_plural': 'bidang_usaha',
                'db_table': 'bidang_usaha',
            },
        ),
        migrations.RemoveField(
            model_name='umkmmodel',
            name='du_bdgusha',
        ),
        migrations.RemoveField(
            model_name='umkmmodel',
            name='du_btkusha',
        ),
        migrations.AddField(
            model_name='umkmmodel',
            name='du_bdgusha',
            field=models.ManyToManyField(to='umkmdata.bidangusaha'),
        ),
        migrations.AddField(
            model_name='umkmmodel',
            name='du_btkusha',
            field=models.ManyToManyField(to='umkmdata.bentukusaha'),
        ),
    ]