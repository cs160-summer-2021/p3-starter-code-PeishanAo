from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def favorite(request):
    return render(request, 'coloring/favorite.html')

def popular(request):
    return render(request, 'coloring/popular.html')

def home(request):
    return render(request, 'coloring/home.html')