# Generated by Django 4.2.5 on 2023-09-20 15:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('direction', models.CharField(choices=[('DN', 'DESIGN'), ('IT', 'IT&ENGINEERING'), ('CS', 'COMPUTER SCIENCE'), ('ML', 'MACHINE LEARNING'), ('PM', 'PRODUCT MANAGEMENT'), ('HR', 'HUMAN RESOURCES')], default='DN', max_length=256)),
                ('desc', models.TextField()),
                ('num_of_lessons', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('students', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
