# Generated by Django 5.0.7 on 2024-07-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0007_alter_curso_codigo_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=13),
        ),
    ]