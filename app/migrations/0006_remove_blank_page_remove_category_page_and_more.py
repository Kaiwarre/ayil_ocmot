# Generated by Django 4.2 on 2023-04-26 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_socseti_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blank',
            name='page',
        ),
        migrations.RemoveField(
            model_name='category',
            name='page',
        ),
        migrations.RemoveField(
            model_name='course',
            name='education',
        ),
        migrations.RemoveField(
            model_name='eduimages',
            name='edu',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='education',
        ),
        migrations.DeleteModel(
            name='Footer',
        ),
        migrations.DeleteModel(
            name='SocSeti',
        ),
        migrations.DeleteModel(
            name='Blank',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='EduImages',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
