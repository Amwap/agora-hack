# Generated by Django 4.0.3 on 2022-08-20 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editor_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='main_frame',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='editor_app.element', verbose_name='Root element'),
            preserve_default=False,
        ),
    ]
