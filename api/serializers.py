from rest_framework import serializers
from .models import Bus, Driver, StopPoint, Student, TravelRegister, TravelRegisterDetail, User

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TravelRegisterSerializer(serializers.ModelSerializer):
    date_hour_start = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    date_hour_end = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = TravelRegister
        fields = '__all__'

class StopPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopPoint
        fields = '__all__'

class TravelRegisterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelRegisterDetail
        fields = '__all__'