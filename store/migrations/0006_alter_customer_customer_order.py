# Generated by Django 4.0.1 on 2022-12-31 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20221231_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.order'),
        ),
    ]