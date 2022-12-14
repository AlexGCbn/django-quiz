# Generated by Django 4.1.3 on 2022-11-14 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('difficulty', models.CharField(max_length=254)),
                ('answers', models.CharField(max_length=512)),
                ('correct_answer', models.CharField(max_length=254)),
                ('question_type', models.CharField(choices=[('multiple', 'Multiple Choice'), ('boolean', 'True/False')], max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.category')),
            ],
        ),
    ]
