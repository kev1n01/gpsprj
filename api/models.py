from django.db import models

# Create your models here.
class Bus(models.Model):
    plate = models.CharField("Plate",primary_key=True, max_length=7,unique=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=7, blank=True, null=True)
    STATUSES = (
        ("ruta","ruta"),
        ("sede","sede"),
    )
    status = models.CharField(max_length=4, choices=STATUSES, default="sede")

    def __str__(self):  
        return '{0},{1}'.format(self.plate,self.status)
    
# Nueva tabla usuario
class User(models.Model):
    username = models.CharField('Name', max_length=50, blank=False, null=False)
    password = models.CharField('Password', max_length=8, blank=False, null=False)
    TYPES = (
        (0,"admin"),
        (1,"student"),
        (2,"driver"),
        (3,"guard"),
    )
    type = models.IntegerField(choices=TYPES, default=1)

    def __str__(self):  
        if self.type == 0:
            self.type = "admin"
        if self.type == 1:
            self.type = "student"
        if self.type == 2:
            self.type = "driver"
        if self.type == 3:
            self.type = "guard"
        
        return '{0},{1}'.format(self.username,self.type)

class Driver(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bus_plate = models.ForeignKey(Bus, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):  
        return '{0},{1}'.format(self.user_id,self.bus_plate)
        
class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=7, blank=True, null=True)

    def __str__(self):  
        return '{0}'.format(self.user_id)

class StopPoint(models.Model):
    label = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=11, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=7, blank=True, null=True)
    
    def __str__(self):  
        return self.label
    
class TravelRegister(models.Model): 
    bus_plate = models.ForeignKey(Bus, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    date_hour_start = models.DateTimeField(null=True,blank=True)
    date_hour_end = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):  
        return '{0},{1},{2}'.format(self.driver_id,self.date_hour_start,self.date_hour_end)

class TravelRegisterDetail(models.Model):
    travel_register_id = models.ForeignKey(TravelRegister, on_delete=models.CASCADE, null=False)
    stop_point_id = models.ForeignKey(StopPoint, on_delete=models.CASCADE, null=False)
    quantity_student = models.IntegerField()
    
    def __str__(self):  
        return '{0},{1},{2}'.format(self.travel_register_id,self.stop_point_id,self.quantity_student)
    