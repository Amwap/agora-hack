# Generated by Django 4.0.3 on 2022-05-18 20:51

import apps.auth_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Имя пользователя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, default='', max_length=15, verbose_name='Телефон')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Персонал')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Верификация')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Список пользователей',
                'unique_together': {('username', 'email', 'phone')},
            },
            managers=[
                ('objects', apps.auth_app.models.UserManager()),
            ],
        ),
    ]
