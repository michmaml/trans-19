# Generated by Django 3.0.4 on 2020-04-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans_19', '0002_auto_20200402_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='dateFrom',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='case',
            name='dateTo',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateBirth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateConfi',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='idNum',
            field=models.CharField(max_length=10),
        ),
    ]
