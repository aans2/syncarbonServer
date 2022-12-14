# Generated by Django 4.1.2 on 2022-10-24 01:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bomba',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Alcool'), (1, 'Diesel')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Combustivel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('valor', models.FloatField()),
                ('bomba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='combustivel.bomba')),
            ],
        ),
    ]
