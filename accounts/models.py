from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.response import Response

User = get_user_model()

class StoreDateColumn(models.Model):
    date = models.CharField(verbose_name="Date",max_length=100)
    def __str__(self):
        return self.date


from django.core.exceptions import ValidationError
from rest_framework.exceptions import ParseError
TIME_SLOTS = ((0, '9:00AM - 10:00AM'), (1, '11:00AM - 12:00PM'),(2, '2:00PM - 3:00PM'),(3, '4:00PM - 5:00PM'))
def validate_appointment(value):
    weekday = value.weekday()
    if weekday==5 or weekday==6:
        raise ValidationError("Appointment will be available on weekdays")
def validate_time_slot(value):
    # print(v2)
    if not value:
        raise ValidationError("Not a correct choice ")
class Appointment(models.Model):
    created_date = models.DateTimeField(auto_now_add=True,)
    participent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participent')
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizer')
    appointment_date = models.DateTimeField(validators=[validate_appointment])
    time_slot = models.PositiveSmallIntegerField(choices=TIME_SLOTS,validators=[validate_time_slot])
    def __str__(self):
        return f'{self.participent}'
@receiver(pre_save,sender=Appointment)
def validating_fields(sender,instance,**kwargs,):
    query = Appointment.objects.filter(appointment_date=instance.appointment_date,time_slot=instance.time_slot)
    if query:
        raise ParseError({"error":"Slot has been booked."})

    