from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title' : 'Django Test',
        'bdata' : 'Welcome to the Django Testing.'
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("<h1>Welcome to the Django.</h1>")

def course(request):
    return HttpResponse("<h1>This is the Course View.</h1>")

def courseDetailsInt(request, courseid):
    return HttpResponse(f"<b>The url on the Course (int) : {courseid}.<b>")

def courseDetailsStr(request, coursestr):
    return HttpResponse(f"<b>The url on the Course (str) : {coursestr}.<b>")

def courseDetailsSlug(request, courseslug):
    return HttpResponse(f"<b>The url on the Course (slug) : {courseslug}.<b>")