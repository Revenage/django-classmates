# Generated by Django 2.0.2 on 2018-02-24 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180224_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('on_duty', models.BooleanField(default=True)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Grade')),
            ],
        ),
    ]
