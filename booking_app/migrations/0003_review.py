# Generated by Django 5.0.6 on 2024-05-17 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_room_booking_user_booking_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(verbose_name=1000)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField()),
                ('deleted', models.DateField(blank=True)),
                ('hotel_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking_app.hotel')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking_app.user')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
