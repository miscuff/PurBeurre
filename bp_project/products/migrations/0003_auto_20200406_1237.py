# Generated by Django 3.0.4 on 2020-04-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200406_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substitute',
            name='products',
            field=models.ManyToManyField(related_name='substitutes', to='products.Product'),
        ),
    ]
