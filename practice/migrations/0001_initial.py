# Generated by Django 3.0.2 on 2020-01-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('artist', models.CharField(max_length=40)),
                ('genre', models.CharField(choices=[('R', 'Рок'), ('E', 'Электроника'), ('P', 'Поп'), ('C', 'Классика'), ('O', 'Саундтреки')], max_length=1)),
            ],
        ),
    ]