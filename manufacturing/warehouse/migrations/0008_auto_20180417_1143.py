# Generated by Django 2.0.2 on 2018-04-17 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_auto_20180416_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asmbentry',
            name='versa_sn',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='asmb_versa_sn', to='warehouse.Versa', to_field='sn'),
        ),
    ]
