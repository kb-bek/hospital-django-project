from django.db import models

class Hospital(models.Model):

    ocpo = models.CharField(
        max_length=4,
        db_index=True,
        blank=True,
        verbose_name='окпо',
        unique=True
    )

    CHOICES = (
        ('Bishkek', 'Bishkek'),
        ('Chui', 'Chui'),
        ('Talas', 'Talas'),
        ('Naryn', 'Naryn'),
        ('Issyk-Kol', 'Issyk-Kol'),
        ('Osh', 'Osh'),
        ('Djalal-Abad', 'Djalal-Abad'),
        ('Batken', 'Batken')
    )
    region = models.CharField(
        max_length=255,
        choices=CHOICES
    )

    amount_emp = models.DecimalField(
        max_digits=2,
        decimal_places=0
    )

    BOOL_CHOICES = (
        (True, 1), (False, 0)
    )

    own = models.BooleanField(
        choices=BOOL_CHOICES
    )

    main_doctor = models.OneToOneField(
        'MainDoctor',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.ocpo

class MainDoctor(models.Model):

    fullname = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name='Ф.И.О'
    )

    passport_pincode = models.CharField(
        max_length=9,
        blank=True,
        verbose_name='ПИН-КОД паспорта'
    )

    age = models.IntegerField(
        blank=True,
        verbose_name='Возраст'
    )

    work_experience = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Стаж работы'
    )

    phone_number = models.CharField(
        max_length=14,
        blank=True,
        verbose_name='Номер телефона'
    )

    doctors_cnnct = models.ForeignKey('AttendingDoctor',
                                on_delete=models.CASCADE,
                                verbose_name='Доктора')
    nurse_connect = models.ForeignKey(
        'Nurse',
        on_delete=models.CASCADE,
        verbose_name='Мед.сестры'
    )

    def __str__(self):
        return self.fullname


class AttendingDoctor(models.Model):

    CHOICES = (
        ('ВРАЧ-ТЕРАПЕВТ', 'ВРАЧ-ТЕРАПЕВТ'),
        ('ВРАЧ-ПЕДИАТР', 'ВРАЧ-ПЕДИАТР'),
        ('ВРАЧ-АЛЛЕРГОЛОГ', 'ВРАЧ-АЛЛЕРГОЛОГ'),
        ('ВРАЧ-УРОЛОГ', 'ВРАЧ-УРОЛОГ'),
        ('ВРАЧ-ХИРУРГ', 'ВРАЧ-ХИРУРГ'),
        ('ВРАЧ-ПСИХИАТР', 'ВРАЧ-ПСИХИАТР'),
        ('ВРАЧ-НАРКОЛОГ', 'ВРАЧ-НАРКОЛОГ'),
        ('ВРАЧ-СТОМАТОЛОГ', 'ВРАЧ-СТОМАТОЛОГ'),
        ('СЕМЕЙНЫЙ ВРАЧ', 'СЕМЕЙНЫЙ ВРАЧ'),
        ('ВРАЧ-РЕНТГЕНОЛОГ', 'ВРАЧ-РЕНТГЕНОЛОГ'),
        ('ВРАЧ-ТРАВМАТОЛОГ-ОРТОПЕД', 'ВРАЧ-ТРАВМАТОЛОГ-ОРТОПЕД'),
        ('ВРАЧ-ОНКОЛОГ', 'ВРАЧ-ОНКОЛОГ'),
        ('ВРАЧ-КАРДИОЛОГ', 'ВРАЧ-КАРДИОЛОГ'),
        ('ВРАЧ-АЛЛЕРГОЛОГ', 'ВРАЧ-АЛЛЕРГОЛОГ'),
        ('ВРАЧ-ФИЗИОТЕРАПЕВТ', 'ВРАЧ-ФИЗИОТЕРАПЕВТ'),
        ('ВРАЧ-ГИНЕКОЛОГ', 'ВРАЧ-ГИНЕКОЛОГ'),
        ('ВРАЧ-НЕВРОПАТОЛОГ', 'ВРАЧ-НЕВРОПАТОЛОГ'),

    )

    specialist = models.CharField(
        max_length=255,
        choices=CHOICES,
        verbose_name='Специализация'
    )

    fullname = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name='Ф.И.О'
    )

    passport_pincode = models.CharField(
        max_length=9,
        blank=True,
        verbose_name='ПИН-КОД паспорта'
    )

    age = models.IntegerField(
        blank=True,
        verbose_name='Возраст'
    )

    work_experience = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Стаж работы'
    )

    phone_number = models.CharField(
        max_length=14,
        blank=True,
        verbose_name='Номер телефона'
    )
    nurse_connect = models.OneToOneField(
        'Nurse',
        on_delete=models.CASCADE,
        verbose_name='Мед-сестры'
    )

    patient_connect = models.ManyToManyField(
        'Patient',
        verbose_name='Пациенты')


    def __str__(self):
        return self.fullname

class Nurse(models.Model):

    fullname = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name='Ф.И.О'
    )

    passport_pincode = models.CharField(
        max_length=9,
        blank=True,
        verbose_name='ПИН-КОД паспорта'
    )

    age = models.IntegerField(
        blank=True,
        verbose_name='Возраст'
    )


    phone_number = models.CharField(
        max_length=14,
        blank=True,
        verbose_name='Номер телефона'
    )

    patient_connect = models.ManyToManyField(
        'Patient',
        verbose_name="Пациенты"
    )

    def __str__(self):
        return self.fullname



class Patient(models.Model):

    fullname = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name='Ф.И.О'
    )

    passport_pincode = models.CharField(
        max_length=9,
        blank=True,
        verbose_name='ПИН-КОД паспорта'
    )

    age = models.IntegerField(
        blank=True,
        verbose_name='Возраст'
    )

    phone_number = models.CharField(
        max_length=14,
        blank=True,
        verbose_name='Номер телефона'
    )

    reason = models.TextField(
        blank=True,
        verbose_name='Причина обращения в больницу'
    )


    def __str__(self):
        return self.fullname

