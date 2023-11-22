# Generated by Django 4.2.7 on 2023-11-22 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField()),
                ('dcls_month', models.CharField(max_length=10)),
                ('save_trm_6', models.CharField(max_length=3, null=True)),
                ('save_trm_12', models.CharField(max_length=3, null=True)),
                ('save_trm_24', models.CharField(max_length=3, null=True)),
                ('save_trm_36', models.CharField(max_length=3, null=True)),
                ('intr_rate_6', models.CharField(max_length=5, null=True)),
                ('intr_rate_12', models.CharField(max_length=5, null=True)),
                ('intr_rate_24', models.CharField(max_length=5, null=True)),
                ('intr_rate_36', models.CharField(max_length=5, null=True)),
                ('join_deny', models.TextField(null=True)),
                ('join_way', models.TextField(null=True)),
                ('spcl_cnd', models.TextField(null=True)),
                ('kor_co_nm', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField()),
                ('dcls_month', models.CharField(max_length=10)),
                ('save_trm_6', models.CharField(max_length=3, null=True)),
                ('save_trm_12', models.CharField(max_length=3, null=True)),
                ('save_trm_24', models.CharField(max_length=3, null=True)),
                ('save_trm_36', models.CharField(max_length=3, null=True)),
                ('intr_rate_6', models.CharField(max_length=5, null=True)),
                ('intr_rate_12', models.CharField(max_length=5, null=True)),
                ('intr_rate_24', models.CharField(max_length=5, null=True)),
                ('intr_rate_36', models.CharField(max_length=5, null=True)),
                ('join_deny', models.TextField(null=True)),
                ('join_way', models.TextField(null=True)),
                ('spcl_cnd', models.TextField(null=True)),
                ('kor_co_nm', models.TextField()),
            ],
        ),
    ]
