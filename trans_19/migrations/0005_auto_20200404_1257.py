# Generated by Django 3.0.4 on 2020-04-04 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trans_19', '0004_auto_20200404_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans_19.Patient'),
        ),
    ]
