# Generated by Django 3.1.5 on 2021-01-19 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=20)),
                ('Contact', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
