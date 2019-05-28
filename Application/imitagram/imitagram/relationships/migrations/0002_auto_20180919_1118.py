# Generated by Django 2.1.1 on 2018-09-19 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relationships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='sink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sink', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relationship',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source', to=settings.AUTH_USER_MODEL),
        ),
    ]