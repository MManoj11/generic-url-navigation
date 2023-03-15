from django.shortcuts import render

# Create your views here.
def samplex(request):
    return render(request,'samplex.html')


def sampley(request):
    return render(request,'sampley.html')