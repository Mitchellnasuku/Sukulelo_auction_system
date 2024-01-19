# Generated by Django 3.2 on 2023-05-19 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_alter_bid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='acc_number',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='payment_method',
            field=models.CharField(choices=[('PAYPAL', 'PAYPAL'), ('VISA CARD', 'VISA CARD'), ('MASTERCARD', 'MASTERCARD')], default='PAYPAL', max_length=50),
        ),
        migrations.AddField(
            model_name='bid',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=50),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=50)),
                ('payment_METHOD', models.CharField(choices=[('PAYPAL', 'PAYPAL'), ('VISA CARD', 'VISA CARD'), ('MASTERCARD', 'MASTERCARD')], default='PAYPAL', max_length=50)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='auction.bid')),
            ],
        ),
    ]
