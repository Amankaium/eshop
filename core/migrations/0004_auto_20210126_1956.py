# Generated by Django 3.1.3 on 2021-01-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='goods',
            field=models.ManyToManyField(blank=True, related_name='order', to='core.Good'),
        ),
    ]
