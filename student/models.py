from django.db import models

class student(models.Model):
    student_name = models.CharField(max_length = 255 , verbose_name = "نام")
    student_family = models.CharField(max_length =350 , verbose_name = "نام خانوادگی")
    student_id = models.CharField(max_length = 255 , verbose_name = "شماره دانشجویی")
    meli_code = models.CharField(max_length = 255 , verbose_name = "کد ملی")
    father_name = models.CharField(max_length = 255 , verbose_name = "نام پدر")
    student_phone = models.CharField(max_length = 255 , verbose_name = "شماره همراه ")
    father_phone = models.CharField (max_length =255 , verbose_name = "شماره همراه پدر")
    mother_phone = models.CharField(max_length =255 , verbose_name = "شماره همراه مادر")
    home_phone = models.CharField(max_length = 255 , verbose_name = "شماره منزل")
    mazhab = models.CharField(max_length = 255 , verbose_name = "مذهب")
    birthyear = models.IntegerField(verbose_name= "سال تولد")
    birthmonth = models.IntegerField(verbose_name = "ماه تولد")
    birthdany = models.IntegerField(verbose_name="روز تولد")
    enter_year = models.IntegerField(verbose_name= "سال ورود")
    reshte = models.CharField(max_length = 300 , verbose_name = "رشته تحصیلی")
    maghta_tahsil = models.CharField(max_length = 255 , verbose_name = "مقطع تحصیلی")
    uni_name = models.CharField(max_length = 255 , verbose_name = "نام دانشگاه")
    daneshkade_name = models.CharField(max_length = 255 , verbose_name = "نام دانشکده")
    bank_id = models.CharField(max_length = 255 , verbose_name = "شماره کارت بانکی")
    address = models.TextField(verbose_name="آدرس محل سکونت")
    pasword = models.CharField(max_length = 255 , verbose_name = "رمز عبور")

    # def __str__(self):
    #     return self.student_name +" " +self.student_family



