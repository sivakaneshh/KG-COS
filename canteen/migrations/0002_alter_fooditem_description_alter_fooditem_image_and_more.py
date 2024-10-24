# Generated by Django 4.2 on 2024-10-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='food_images/'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]