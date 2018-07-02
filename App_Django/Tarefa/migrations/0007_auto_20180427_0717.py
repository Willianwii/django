# Generated by Django 2.0.2 on 2018-04-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarefa', '0006_tarefa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(blank=True, choices=[('CANC', 'Cancelada'), ('CONC', 'Concluida')], default='', max_length=5, verbose_name='Status'),
        ),
    ]
