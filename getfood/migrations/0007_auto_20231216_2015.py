# Generated by Django 3.2.23 on 2023-12-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfood', '0006_orderproducts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderProducts',
            new_name='OrderProduct',
        ),
        migrations.AlterModelOptions(
            name='consumer',
            options={'verbose_name': 'Consumer', 'verbose_name_plural': 'Consumers'},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'Provider', 'verbose_name_plural': 'Providers'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
