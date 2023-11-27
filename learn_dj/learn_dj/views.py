from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title' : 'Django Test',
        'bdata' : 'Welcome to the Django Testing.',
        'clist' : [ 'PHP', 'Java', 'Django', 'Python' ],
        'numbers' : [10,20,30,40,50,60,70],
        'student_details' : [
            { 'name' : 'Rohit', 'phone' : 9878754266},
            { 'name' : 'Deepak', 'phone' : 9878754244},
            { 'name' : 'Kapil', 'phone' : 9878754222}
        ] 
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return render(request, "about.html")

def course(request):
    return HttpResponse("<h1>This is the Course View.</h1>")

def courseDetailsInt(request, courseid):
    return HttpResponse(f"<b>The url on the Course (int) : {courseid}.<b>")

def courseDetailsStr(request, coursestr):
    return HttpResponse(f"<b>The url on the Course (str) : {coursestr}.<b>")

def courseDetailsSlug(request, courseslug):
    return HttpResponse(f"<b>The url on the Course (slug) : {courseslug}.<b>")