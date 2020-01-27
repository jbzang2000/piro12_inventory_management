# Generated by Django 2.2.9 on 2020-01-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('shops', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('items', models.ManyToManyField(blank=True, to='inventorymanage.Item')),
            ],
        ),
    ]