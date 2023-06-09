# Generated by Django 4.0.3 on 2023-04-22 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Masters', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('modifiedon', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.SmallIntegerField(default=1, null=True)),
                ('createdby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='countrycreated', to=settings.AUTH_USER_MODEL)),
                ('modifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='countryupdated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='cities', to='Masters.country'),
        ),
    ]
