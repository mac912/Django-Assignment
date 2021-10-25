# Generated by Django 3.2.8 on 2021-10-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('author_name', models.CharField(max_length=30)),
            ],
        ),
    ]