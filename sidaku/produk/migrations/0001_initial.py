# Generated by Django 4.1 on 2022-11-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdukModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komoditi', models.CharField(max_length=150)),
                ('volume', models.CharField(max_length=150)),
                ('satuan', models.CharField(max_length=150)),
                ('harga', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fotoprod', models.ImageField(blank=True, null=True, upload_to='produk/')),
            ],
            options={
                'verbose_name_plural': 'produk_data',
                'db_table': 'produk_data',
            },
        ),
    ]
