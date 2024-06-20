from django.shortcuts import render

def index(request):
    return render(request, 'webcam_app/index.html')

