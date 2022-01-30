# Generated by Django 4.0.1 on 2022-01-30 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pay', models.PositiveIntegerField()),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salary.industry')),
            ],
            options={
                'verbose_name': 'Job Board',
                'verbose_name_plural': 'Job Board',
            },
        ),
    ]
