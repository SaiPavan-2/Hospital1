# Generated by Django 4.0.3 on 2022-09-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_doctors_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('bloodgroup', models.CharField(max_length=200)),
                ('no_of_units_available', models.IntegerField(default=0)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
    ]