# Generated by Django 3.1.5 on 2021-02-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='team',
            name='prof_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
