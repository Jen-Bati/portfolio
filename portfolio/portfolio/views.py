from django.shortcuts import render

def aboutme(request):
    context = {'aboutme':'active'}
    return render(request,"aboutme.html", context)

def education(request):
    context = {'education':'active'}
    return render(request,"education.html", context)

def training(request):
    context = {'training':'active'}
    return render(request,"training.html", context)

def respro(request):
    context = {'respro':'active'}
    return render(request,"respro.html", context)

def gallery(request):
    context = {'gallery':'active'}
    return render(request,"gallery.html", context)

def contact(request):
    context = {'contact':'active'}
    return render(request,"contact.html", context)

def download(request):
    context = {'download':'active'}
    return render(request,"download.html", context)