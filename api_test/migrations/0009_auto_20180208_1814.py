# Generated by Django 2.0.2 on 2018-02-08 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0008_auto_20180208_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdynamic',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectInfo', to='api_test.Project', verbose_name='所属项目'),
        ),
    ]
