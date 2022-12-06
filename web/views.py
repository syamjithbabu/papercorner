from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')

def gallery(request):
    return render(request,'web/gallery.html')

def blog(request):
    return render(request,'web/blog.html')

def contact(request):
    return render(request,'web/contact.html')