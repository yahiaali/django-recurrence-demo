# Generated by Django 2.0.6 on 2018-06-25 19:43

from django.db import migrations, models
import recurrence.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('recurrences', recurrence.fields.RecurrenceField()),
            ],
        ),
    ]
