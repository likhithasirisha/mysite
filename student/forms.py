from django import forms
from .models import Student
from .models import Employee
from .models import Movie
from .models import Car
from .models import Bus
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):

   class Meta:
    model= Student
    fields= ['name','mobile']

class EmployeeForm(forms.ModelForm):

   class Meta:
      model= Employee
      fields=['name','department','salary']

class MovieForm(forms.ModelForm):
   class Meta:
      model= Movie
      fields= ['name','director','Hero','Heroine','release_year']

class CarForm(forms.ModelForm):
   class Meta:
      model= Car
      fields=['name','color','price','mileage','year','fuel_type','location']

class BusForm(forms.ModelForm):
   class Meta:
      model= Bus
      fields=['bus_number','destination','departure_time','arrival_time','price','bus_type','bus_company','seats_available']

   def clean_bus_number(self):
      bus_number = self.cleaned_data.get('bus_number')
      if (bus_number)!=200:
         raise ValidationError("Number should be more than 200")
      return bus_number

   