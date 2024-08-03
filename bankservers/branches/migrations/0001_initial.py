# Generated by Django 4.2.14 on 2024-08-02 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11, unique=True)),
                ('branch', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='branches.bank')),
            ],
        ),
    ]
