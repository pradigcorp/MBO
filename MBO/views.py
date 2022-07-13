from django.shortcuts import render

# Create your views here.

def home(request):
    form = 'hello'
    return render(request, 'MBO/home.html', {'form': form})
