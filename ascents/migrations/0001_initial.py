# Generated by Django 2.0.2 on 2018-06-30 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ascent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ascent', models.DateField()),
                ('style', models.CharField(choices=[('fl', 'fl'), ('rp', 'rp'), ('os', 'os')], max_length=2)),
                ('points', models.IntegerField()),
            ],
            options={
                'ordering': ['-points', '-date_ascent'],
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('crag', models.CharField(max_length=30)),
                ('sector', models.CharField(blank=True, max_length=30)),
                ('grade', models.CharField(choices=[('6a', '6a'), ('6a+', '6a+'), ('6b', '6b'), ('6b+', '6b+'), ('6c', '6c'), ('6c+', '6c+'), ('7a', '7a'), ('7a+', '7a+'), ('7b', '7b'), ('7b+', '7b+'), ('7c', '7c'), ('7c+', '7c+'), ('8a', '8a'), ('8a+', '8a+'), ('8b', '8b'), ('8b+', '8b+'), ('8c', '8c'), ('8c+', '8c+'), ('9a', '9a'), ('9a+', '9a+'), ('9b', '9b'), ('9b+', '9b+')], max_length=3)),
                ('user', models.ManyToManyField(through='ascents.Ascent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ascent',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ascents.Route'),
        ),
        migrations.AddField(
            model_name='ascent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ascents', to=settings.AUTH_USER_MODEL),
        ),
    ]
