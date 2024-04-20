from django.db import models

class Student(models.Model):
    GENDER_CHOICES=[
        ('Male','male'),
        ('Female','female'),
    ]
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=200,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=15,choices=GENDER_CHOICES,null=True,blank=True)    
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name= models.CharField(max_length=20)
    department= models.CharField(max_length=100)
    salary=models.IntegerField()
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    name= models.CharField(max_length=20)
    director= models.CharField(max_length=100)
    Hero= models.CharField(max_length=30)
    Heroine= models.CharField(max_length=20)
    release_year= models.IntegerField()

    def __str__(self):
        return self.name

class Car(models.Model):
    name= models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    mileage = models.IntegerField()
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=30)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bus(models.Model):
    bus_number= models.IntegerField(null=True,blank=True)
    destination= models.CharField(max_length=50,null=True,blank=True)
    departure_time= models.TimeField()
    arrival_time= models.TimeField()
    price= models.IntegerField(null=True,blank=True)
    bus_type= models.CharField(max_length=20,null=True,blank=True)
    bus_company= models.CharField(max_length=20,null=True,blank=True)
    seats_available= models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.bus_number)


