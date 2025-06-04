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
            'title':'QA Automated retail analysis',
            #'path': 'fifa_world_cup.jpeg',
            'link': 'https://github.com/Svarsha12/qa-automated-retail-analysis.git',
            'description': 'This project demonstrates a complete data pipeline integrating QA automation, data governance, analytics, and interactive dashboards using a realistic retail sales dataset. It showcases how to ensure data quality, perform validation using Pytest, document metadata, and visualize both business and QA metrics using Tableau.'
        },
        {
            'title':'Book to Scrape Project-BDD Automation',
            #'path': 'heart-disease.jpeg',
            'link': 'https://github.com/Svarsha12/scraping_automation_project.git',
            'description': 'A Python-based automation project that combines Selenium, BDD with Behave, and BeautifulSoup to scrape data from the Books to Scrape website, specifically targeting the Music category. The scraped data is structured into a Pandas DataFrame and exported to a CSV file for further analysis.'
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

