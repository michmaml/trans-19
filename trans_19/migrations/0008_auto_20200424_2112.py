# Generated by Django 3.0.4 on 2020-04-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans_19', '0007_auto_20200404_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='caseNum',
            field=models.IntegerField(verbose_name='Case Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateBirth',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dateConfi',
            field=models.DateField(verbose_name='Date of Confirmation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='idNum',
            field=models.CharField(max_length=10, verbose_name='ID Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
    ]
