from rest_framework import serializers
from .models import *
class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        exclude =['participent']
