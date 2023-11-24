from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to the Django.")