# Generated by Django 4.2.6 on 2023-11-08 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=50)),
                ('aroma', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('U', 'Unisex')], max_length=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fragancia.cliente')),
                ('perfume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fragancia.perfume')),
            ],
        ),
    ]
