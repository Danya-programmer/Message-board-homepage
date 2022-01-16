from msilib.schema import ListView
from django.forms import models
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView): 
    model = Post    
    template_name = "home.html"
    
# Create your views here.
