# Generated by Django 4.0.4 on 2022-05-20 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendingDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist', models.CharField(choices=[('ВРАЧ-ТЕРАПЕВТ', 'ВРАЧ-ТЕРАПЕВТ'), ('ВРАЧ-ПЕДИАТР', 'ВРАЧ-ПЕДИАТР'), ('ВРАЧ-АЛЛЕРГОЛОГ', 'ВРАЧ-АЛЛЕРГОЛОГ'), ('ВРАЧ-УРОЛОГ', 'ВРАЧ-УРОЛОГ'), ('ВРАЧ-ХИРУРГ', 'ВРАЧ-ХИРУРГ'), ('ВРАЧ-ПСИХИАТР', 'ВРАЧ-ПСИХИАТР'), ('ВРАЧ-НАРКОЛОГ', 'ВРАЧ-НАРКОЛОГ'), ('ВРАЧ-СТОМАТОЛОГ', 'ВРАЧ-СТОМАТОЛОГ'), ('СЕМЕЙНЫЙ ВРАЧ', 'СЕМЕЙНЫЙ ВРАЧ'), ('ВРАЧ-РЕНТГЕНОЛОГ', 'ВРАЧ-РЕНТГЕНОЛОГ'), ('ВРАЧ-ТРАВМАТОЛОГ-ОРТОПЕД', 'ВРАЧ-ТРАВМАТОЛОГ-ОРТОПЕД'), ('ВРАЧ-ОНКОЛОГ', 'ВРАЧ-ОНКОЛОГ'), ('ВРАЧ-КАРДИОЛОГ', 'ВРАЧ-КАРДИОЛОГ'), ('ВРАЧ-АЛЛЕРГОЛОГ', 'ВРАЧ-АЛЛЕРГОЛОГ'), ('ВРАЧ-ФИЗИОТЕРАПЕВТ', 'ВРАЧ-ФИЗИОТЕРАПЕВТ'), ('ВРАЧ-ГИНЕКОЛОГ', 'ВРАЧ-ГИНЕКОЛОГ'), ('ВРАЧ-НЕВРОПАТОЛОГ', 'ВРАЧ-НЕВРОПАТОЛОГ')], max_length=255, verbose_name='Специализация')),
                ('fullname', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Ф.И.О')),
                ('passport_pincode', models.CharField(blank=True, max_length=9, verbose_name='ПИН-КОД паспорта')),
                ('age', models.IntegerField(blank=True, verbose_name='Возраст')),
                ('work_experience', models.CharField(blank=True, max_length=255, verbose_name='Стаж работы')),
                ('phone_number', models.CharField(blank=True, max_length=14, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocpo', models.CharField(blank=True, db_index=True, max_length=4, unique=True, verbose_name='окпо')),
                ('region', models.CharField(choices=[('Bishkek', 'Bishkek'), ('Chui', 'Chui'), ('Talas', 'Talas'), ('Naryn', 'Naryn'), ('Issyk-Kol', 'Issyk-Kol'), ('Osh', 'Osh'), ('Djalal-Abad', 'Djalal-Abad'), ('Batken', 'Batken')], max_length=255)),
                ('amount_emp', models.DecimalField(decimal_places=0, max_digits=2)),
                ('own', models.BooleanField(choices=[(True, 1), (False, 0)])),
                ('main_doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.attendingdoctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Ф.И.О')),
                ('passport_pincode', models.CharField(blank=True, max_length=9, verbose_name='ПИН-КОД паспорта')),
                ('age', models.IntegerField(blank=True, verbose_name='Возраст')),
                ('phone_number', models.CharField(blank=True, max_length=14, verbose_name='Номер телефона')),
                ('reason', models.TextField(blank=True, verbose_name='Причина обращения в больницу')),
                ('hospital_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hospital', verbose_name='Больница')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Ф.И.О')),
                ('passport_pincode', models.CharField(blank=True, max_length=9, verbose_name='ПИН-КОД паспорта')),
                ('age', models.IntegerField(blank=True, verbose_name='Возраст')),
                ('phone_number', models.CharField(blank=True, max_length=14, verbose_name='Номер телефона')),
                ('hospital_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hospital', verbose_name='Больница')),
                ('patient_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient', verbose_name='Пациенты')),
            ],
        ),
        migrations.CreateModel(
            name='MainDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Ф.И.О')),
                ('passport_pincode', models.CharField(blank=True, max_length=9, verbose_name='ПИН-КОД паспорта')),
                ('age', models.IntegerField(blank=True, verbose_name='Возраст')),
                ('work_experience', models.CharField(blank=True, max_length=255, verbose_name='Стаж работы')),
                ('phone_number', models.CharField(blank=True, max_length=14, verbose_name='Номер телефона')),
                ('doctors_cnnct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attendingdoctor', verbose_name='Доктора')),
            ],
        ),
        migrations.AddField(
            model_name='attendingdoctor',
            name='hospital_connect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hospital', verbose_name='Больница'),
        ),
        migrations.AddField(
            model_name='attendingdoctor',
            name='nurse_connect',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.nurse', verbose_name='Мед-сестры'),
        ),
        migrations.AddField(
            model_name='attendingdoctor',
            name='patient_connect',
            field=models.ManyToManyField(to='app.patient', verbose_name='Пациенты'),
        ),
    ]