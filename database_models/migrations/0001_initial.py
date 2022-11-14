# Generated by Django 4.1.2 on 2022-11-10 11:53

import database_models.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.TextField(default=0, max_length=12, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('alias_name', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(blank=True, max_length=16, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=32, null=True)),
                ('bio', models.TextField(blank=True, max_length=300, null=True, verbose_name='bio')),
                ('social_link', models.TextField(blank=True, null=True)),
                ('donation_link', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=database_models.models.get_profile_pic_path)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('book_name', models.CharField(default='Untitled', max_length=60)),
                ('description', models.TextField(blank=True, max_length=120)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('book_type', models.IntegerField(default=1)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=database_models.models.get_thumbnail_path)),
                ('pdf_files', models.FileField(blank=True, null=True, upload_to=database_models.models.get_pdf_files_path)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_list', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=40)),
                ('msg', models.TextField(blank=True, max_length=100)),
                ('book_refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_models.book')),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=40)),
                ('msg', models.TextField(max_length=500)),
                ('book_refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_models.book')),
                ('issuer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='database_models.genre'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.FloatField(default=0)),
                ('title', models.CharField(max_length=40)),
                ('msg', models.TextField(max_length=500)),
                ('is_edited', models.BooleanField(default=False)),
                ('last_edited', models.DateTimeField(null=True)),
                ('book_refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_models.book')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('reviewer', 'book_refer')},
            },
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_read_latest_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('book_refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_models.book')),
                ('user_refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_refer', 'book_refer')},
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_models.book')),
                ('user_refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_refer', 'book_refer')},
            },
        ),
    ]