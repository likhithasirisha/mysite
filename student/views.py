from django.shortcuts import render,redirect
from .models import Student
from .models import Employee
from .models import Movie
from .models import Car
from .models import Bus
from .forms import StudentForm
from .forms import EmployeeForm
from .forms import MovieForm
from .forms import CarForm
from .forms import BusForm


def student_list_view(request):
    #obj= Student.objects.get(id=3)
    #obj= Student.objects.filter(id=3)
    obj= Student.objects.all()
    
    context={
        'students': obj
    }
    return render(request,'student_list.html', context)

def update_student_view(request,id):
    obj = Student.objects .get(pk=id)
    if  request.method =="POST":
       form = StudentForm(request.POST,instance=obj)
       if form.is_valid():
         form.save()
       else:
        print("invalid form")
    s_form =  StudentForm(instance=obj) 
    return render(request,'update_student.html', {'form':s_form})

def student_detail_view(request,id):
    obj= Student.objects .get(pk=id)
    context={
        'student':obj
    }
    return render(request,'student_detail.html',context)

def create_student_view(request):
    if request.method =="POST":
        #stud_name=request.POST.get("student_nam")
        #stud_mobile=request.POST.get("student_mobile")
        #obj = Student(name=stud_name,mobile=stud_mobile)
        #obj.save()
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()

    form= StudentForm()
    return render(request,'create_student.html',{'form':form})

def delete_student_view(request,id):
    obj= Student.objects.get(pk=id)
    obj.delete()
    return redirect("/")

def employee_list_view(request):
    employees= Employee.objects.all()
    context={
        'employee':employees
    }
    return render(request,'employee_list.html',context)

def create_employee_view(request):
    if request.method =="POST":
        form= EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    form= EmployeeForm()
    return render(request,'create_employee.html',{'form':form})

def employee_detail_view(request,id):
    employees= Employee.objects.get(pk=id)
    context={
        'employee':employees
    }
    return render(request,'employee_detail.html',context)

def update_employee_view(request,id):
    employees = Employee.objects.get(pk=id)
    if request.method =="POST":
        form = EmployeeForm(request.POST,instance=employees)
        if form.is_valid():
            form.save()
        else:
            print("invalid form")
    s_form = EmployeeForm(instance=employees)
    return render(request,'update_employee.html',{'form':s_form})

def delete_employee_view(request,id):
    employees= Employee.objects.get(pk=id)
    employees.delete()
    return redirect("/")

def movie_list_view(request):
     movies= Movie.objects.all()
     context={
        'movie': movies
     }
     return render(request,'movie_list.html',context)

def create_movie_view(request):
    if request.method =="POST":
        form= MovieForm(request.POST)
        if form.is_valid():
            form.save()
    form= MovieForm()
    return render(request,'create_movie.html',{'form':form})

def movie_detail_view(request,id):
    movies= Movie.objects.get(pk=id)
    context={
        'movie':movies
    }
    return render(request,'movie_detail.html',context)

def update_movie_view(request,id):
    movies = Movie.objects.get(pk=id)
    if request.method =="POST":
        form = MovieForm(request.POST,instance=movies)
        if form.is_valid():
            form.save()
        else:
            print("invalid form")
    s_form= MovieForm(instance=movies)
    return render(request,'update_movie.html',{'form':s_form})

def delete_movie_view(request,id):
    movies= Movie.objects.get(pk=id)
    movies.delete()
    return redirect("/")

def car_list_view(request):
    cars= Car.objects.all()
    context={
        'car': cars
    }
    return render(request,'car_list.html',context)

def create_car_view(request):
    if request.method =="POST":
        form= CarForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'create_car.html',{'form':form})
        
    form= CarForm()
    return render(request,'create_car.html',{'form':form})

def car_detail_view(request,id):
    cars= Car.objects.get(pk=id)
    context={
        'car':cars
    }
    return render(request,'car_detail.html',context)

def update_car_view(request,id):
    cars= Car.objects.get(pk=id)
    if request.method =="POST":
        form = CarForm(request.POST,instance=cars)
        if form.is_valid():
            form.save()
        else:
            print("invalid form")
    s_form= CarForm(instance=cars)
    return render(request,'update_car.html',{'form':s_form})

def delete_car_view(request,id):
    cars= Car.objects.get(pk=id)
    cars.delete()
    return redirect("/")

def bus_list_view(request):
    buses= Bus.objects.all()
    context={
        'bus': buses
    }
    return render(request,'bus_list.html',context)

def create_bus_view(request):
    if request.method == "POST":
        form= BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request,'create_bus.html',{'form':form})
    else:
        form= BusForm()
    return render(request,'create_bus.html',{'form':form})

def bus_detail_view(request,id):
    buses= Bus.objects.get(pk=id)
    context={
        'bus':buses
    }
    return render(request,'bus_detail.html',context)

def update_bus_view(request,id):
    buses= Bus.objects.get(pk=id)
    if request.method =="POST":
        form = BusForm(request.POST,instance=buses)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request,'update_bus.html',{'form':form})
    else:
        form = BusForm(instance=buses)
    return render(request,'update_bus.html',{'form':form})

def delete_bus_view(request,id):
    buses= Bus.objects.get(pk=id)
    buses.delete()
    return redirect("/")

def table_view(request):
    return render(request,'table.html')

def card_view(request):
    return render(request,'card.html')

def accordion_view(request):
    return render(request,'accordion.html')



