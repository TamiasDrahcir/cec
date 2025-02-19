# Generated by Django 5.1 on 2024-11-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cec', '0007_operatormodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatorReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RES', models.IntegerField()),
                ('ACB', models.IntegerField()),
                ('SCI', models.IntegerField()),
                ('THE', models.IntegerField()),
                ('GYM', models.IntegerField()),
                ('RESL', models.IntegerField()),
                ('ACBL', models.IntegerField()),
                ('SCIL', models.IntegerField()),
                ('THEL', models.IntegerField()),
                ('GYML', models.IntegerField()),
                ('RESE', models.IntegerField()),
                ('ACBE', models.IntegerField()),
                ('SCIE', models.IntegerField()),
                ('THEE', models.IntegerField()),
                ('GYME', models.IntegerField()),
                ('RESA', models.IntegerField()),
                ('ACBA', models.IntegerField()),
                ('SCIA', models.IntegerField()),
                ('THEA', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='OperatorModels',
        ),
    ]
