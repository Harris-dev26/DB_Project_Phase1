# Generated by Django 4.1.3 on 2022-12-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourists', '0016_bookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='edate',
            field=models.DateField(verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Customer Name'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='sdate',
            field=models.DateField(verbose_name='Start date'),
        ),
    ]
