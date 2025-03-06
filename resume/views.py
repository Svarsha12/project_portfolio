from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    projects_show=[
        {
            'title':'fifa_worldcup',
            'path': 'fifa_world_cup.jpeg',
            'link': 'https://github.com/Svarsha12/fifa_worldcup'
        },
        {
            'title':'cardiovascular-disease',
            'path': 'heart-disease.jpeg',
            'link': 'https://github.com/Svarsha12/cardiovascular-disease/tree/main'
        }
    
  
        
    ]
    return render (request, "projects.html",{"projects_show":projects_show})




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = ContactForm()  # Create an empty form for GET requests

    return render(request, 'contact.html', {'form': form})
def success(request):
    return render(request, 'success.html')

def blog(request):
    return render(request,"blog.html")

