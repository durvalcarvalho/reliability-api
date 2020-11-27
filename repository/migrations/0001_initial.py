# Generated by Django 3.1.3 on 2020-11-27 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsyncTask',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('image', models.URLField(null=True)),
                ('url', models.URLField()),
                ('must_have_labels', models.CharField(max_length=500)),
                ('must_not_have_labels', models.CharField(max_length=500)),
                ('failed', models.BooleanField()),
                ('finished', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('must_have_labels', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Repositories',
                'unique_together': {('url', 'must_have_labels')},
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField()),
                ('html_url', models.URLField()),
                ('api_url', models.URLField()),
                ('is_closed', models.BooleanField()),
                ('labels', models.ManyToManyField(to='repository.Label')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='repository.repository')),
            ],
        ),
    ]
