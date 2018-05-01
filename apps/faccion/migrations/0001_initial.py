# Generated by Django 2.0.4 on 2018-05-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('partidasGanadas', models.IntegerField()),
                ('partidasPerdidas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('partidasGanadas', models.IntegerField()),
                ('partidasPerdidas', models.IntegerField()),
                ('caster', models.ManyToManyField(to='faccion.Caster')),
            ],
        ),
    ]
