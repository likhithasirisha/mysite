from django.shortcuts import render

# Create your views here.
def about_us_view(request):
   if request.method== "GET":
    context={
        'key':'value',
        'name':'sirisha',
        'greeting':'hello',
        'street':'jp nagar'
    }
    return render(request, 'index.html' , context)

def logout_view(request):
    if request.method =="GET":
     context={
        'institute':'aadiguru',
        'pg':'sai ranga',
        'fruit':'banana',
        'number':12345,
        'key':'django',
        'greet':'hello siri',
        'animal':'lion'
     }
     return render(request, 'logout.html' ,context)