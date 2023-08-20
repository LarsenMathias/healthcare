# Generated by Django 4.1.3 on 2023-08-20 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareapp', '0003_customuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='blog_image/')),
                ('Summary', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('draft', models.CharField(choices=[('upload', 'Upload'), ('draft', 'Draft')], default='draft', max_length=10)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcareapp.category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]