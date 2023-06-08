# Generated by Django 4.0.4 on 2022-05-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('Description', models.TextField()),
                ('category', models.CharField(max_length=256)),
                ('subcategory1', models.CharField(max_length=265)),
                ('subcategory2', models.CharField(max_length=256)),
                ('subcategory3', models.CharField(max_length=256)),
                ('prd_img', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
