# Generated by Django 2.2.24 on 2021-07-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210720_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefits',
            options={'verbose_name': 'Advantage', 'verbose_name_plural': 'Benefits'},
        ),
        migrations.AlterModelOptions(
            name='brands',
            options={'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='promoslider',
            options={'verbose_name': 'Promo', 'verbose_name_plural': 'Promotions'},
        ),
        migrations.AddField(
            model_name='products',
            name='is_new',
            field=models.BooleanField(db_index=True, default=True, verbose_name='product_new'),
        ),
        migrations.AlterField(
            model_name='benefits',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(blank=True, max_length=128, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='products',
            name='screen',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3, verbose_name='screen'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sim',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='sim_qty'),
        ),
        migrations.AlterField(
            model_name='products',
            name='storage',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='storage'),
        ),
    ]