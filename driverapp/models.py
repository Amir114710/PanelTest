from django.db import models

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=1000, verbose_name='نام رنگ')

    def __str__(self):
        return self.name

class DeviceTypes(models.Model):
    name = models.CharField(max_length=10000, verbose_name='نام وسیله')   

    def __str__(self):
        return self.name


class CartTypes(models.Model):
    name = models.CharField(max_length=1000, verbose_name='مدل ماشین')

    def __str__(self):
        return self.name
class BusInformation(models.Model):
    device_color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='bus', verbose_name='رنگ وسیله')
    device_type = models.ForeignKey(DeviceTypes, on_delete=models.CASCADE, related_name='bus', verbose_name='نوع وسیله')
    plaque = models.CharField(max_length=20, verbose_name='نام پلاک')
    car_name = models.CharField(max_length=1000, verbose_name='نام ماشین') 
    name_car_owner = models.CharField(max_length=1000, verbose_name='نام صاجب خودرو')
    capacity_number = models.CharField(max_length=10000, verbose_name='تعداد ظرفیت')
    car_type = models.ForeignKey(CartTypes, on_delete=models.CASCADE, verbose_name='مدل ماشین')
    granny = models.BooleanField(default=False, verbose_name='سیستم گرمایش')
    cooling = models.BooleanField(default=False, verbose_name='سیستم سرمایش')
    cost = models.DecimalField(verbose_name='هزینه')
    date = models.DateField(verbose_name='تاریخ')
    origin = models.CharField(max_length=10000, verbose_name='مبدا')
    destination = models.CharField(max_length=1000, verbose_name='مقصد')
    service_date = models.DateField(verbose_name='مدت تاریخ سرویس دادن')
    entity = models.TimeField(verbose_name='ساعت حرکت')
    time_destination = models.TimeField(verbose_name='ساعت رسیدن به مقصد')
    service_company_name = models.CharField(max_length=10000, verbose_name=' نام شرکت ارائه دهنده سرویس')
    is_public = models.BooleanField(default=False)

class Comment(models.Model):
    car_post = models.ForeignKey(BusInformation, on_delete=models.CASCADE, related_name='comment', verbose_name='اگهی اتوبوس')
    name = models.CharField(max_length=1000, verbose_name='نام' )
    body = models.TextField(max_length=10000000, verbose_name='جزعیات نظر')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='reply', verbose_name='ریپلای')

    def __str__(self):
        return self.name
    
