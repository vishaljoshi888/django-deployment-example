from django.shortcuts import render


def index(request):
    ran_dict = {'name': "Vishal Joshi",'number': 888}
    return render(request, 'ravi_app/index.html',ran_dict)


def other(request):
    return render(request, 'ravi_app/other.html')


def actual(request):
    return render(request, 'ravi_app/actual.html')

# Create your views here.
