# Generated by Django 3.1.5 on 2021-01-28 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210126_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='All',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.order')),
            ],
            bases=('core.order',),
        ),
    ]
