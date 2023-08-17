# Generated by Django 4.2.4 on 2023-08-17 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='code',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='role',
            name='code',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='role', to='acl.permission'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='acl.role'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='role', to=settings.AUTH_USER_MODEL),
        ),
    ]
