# Generated by Django 4.2 on 2024-11-05 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0002_alter_fooditem_description_alter_fooditem_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0006_alter_orders_payment_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='canteen.fooditem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]