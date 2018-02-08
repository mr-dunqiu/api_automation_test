# Generated by Django 2.0.1 on 2018-02-08 08:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_test', '0006_remove_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(through='api_test.ProjectMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
