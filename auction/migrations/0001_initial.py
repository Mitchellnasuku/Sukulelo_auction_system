# Generated by Django 3.2 on 2023-05-13 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('Home Equipment', 'Home Equipment'), ('Office Equipment', 'Office Equipment'), ('Cars', 'Cars'), ('Clothes', 'Clothes')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.CharField(choices=[('Won Bid', 'Won Bid'), ('Current Bid', 'Current Bid'), ('Outbid', 'Outbid'), ('Lost Bid', 'Lost Bid')], default='Current Bid', max_length=50)),
                ('date_placed', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auction_item', to='auction.item')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='auction.person')),
            ],
        ),
    ]
