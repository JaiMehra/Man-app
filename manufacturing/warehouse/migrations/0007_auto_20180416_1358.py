# Generated by Django 2.0.2 on 2018-04-16 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_auto_20180416_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asmbentry',
            name='task_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_id', to='warehouse.Task'),
        ),
    ]
