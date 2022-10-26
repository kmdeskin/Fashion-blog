from django.views import generic
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def index(request):
     template = loader.get_template('MyApp/index.html')
     context = {}
     return HttpResponse(template.render(context, request))

     



    
