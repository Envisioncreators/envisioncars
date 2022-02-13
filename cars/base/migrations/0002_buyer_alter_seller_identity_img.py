# Generated by Django 4.0 on 2022-02-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('phone_wa', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('identity', models.CharField(max_length=50)),
                ('identity_no', models.CharField(max_length=20)),
                ('identity_img', models.ImageField(blank=True, null=b'I01\n', upload_to='images')),
                ('address_temp', models.TextField()),
                ('address', models.TextField()),
                ('buyer_type', models.CharField(max_length=20)),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='seller',
            name='identity_img',
            field=models.ImageField(blank=True, null=b'I01\n', upload_to='images'),
        ),
    ]