# Generated by Django 4.0.4 on 2022-05-31 17:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('surname', models.CharField(max_length=255, verbose_name='Surname')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('phone2', models.CharField(max_length=255, verbose_name='Phone2')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('is_pinned', models.BooleanField(default=False, verbose_name='Pin')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255, verbose_name='Course name')),
                ('about', models.TextField(verbose_name='About')),
                ('course_details', models.TextField(default='0', verbose_name='Details')),
                ('duration', models.CharField(default='1', max_length=255, verbose_name='Course Duration')),
                ('courseType', models.CharField(default='0', max_length=255, verbose_name='CourseType')),
                ('image', models.ImageField(upload_to='img/%y/%m/%d/', verbose_name='Choose image main (format: jpg, jpeg, png)')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('answer', models.CharField(max_length=655, verbose_name='Answer')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitors', models.IntegerField(default=0, verbose_name='Visitors')),
                ('visits', models.IntegerField(default=0, verbose_name='Visits')),
                ('registerated', models.IntegerField(default=0, verbose_name='Registerated')),
                ('is_new', models.BooleanField(default=False, verbose_name='Is New')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='img/%y/%m/%d/', verbose_name='Choose image main (format: jpg, jpeg, png)')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('phone1', models.CharField(max_length=255)),
                ('phone2', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('tiktok', models.CharField(max_length=255, verbose_name='@Tiktok')),
                ('instagram', models.CharField(max_length=255, verbose_name='@Instagram')),
                ('telegram', models.CharField(max_length=255, verbose_name='@Telegram')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=255, verbose_name='Teacher name')),
                ('about', models.TextField(verbose_name='About')),
                ('image', models.ImageField(upload_to='img/%y/%m/%d/', verbose_name='Choose image main (format: jpg, jpeg, png)')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
