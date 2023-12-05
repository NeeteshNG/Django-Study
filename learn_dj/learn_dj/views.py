from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm

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
    if request.method=="GET":
        name=request.GET.get('name')
    return render(request, "about.html", {"name" : name})

def contact(request):
    return render(request, "contact.html")

def marksheet(request):
    return render(request, "marksheet.html")

def calculator(request):
    c=''
    o_e = ''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("num1"))
            n2=eval(request.POST.get("num2"))
            opr=request.POST.get("opr")
            if opr=="+":
                c = n1 + n2
            elif opr=="-":
                c = n1 - n2
            elif opr=="*":
                c = n1 * n2
            elif opr=="/":
                c = n1 / n2
            
            if c%2==0:
                o_e = 'EVEN'
            else:
                o_e = 'ODD'
    except:
        c="Invalid Operations."
    return render(request, "calculator.html", {'calculation': c, 'odd_even' : o_e})

def user(request):
    fn = usersForm()
    data = {'form' : fn}
    try:
        if request.method=="POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            data={
                'form' : fn,
                'fname' : fname, 
                'lname' : lname,
                'name' : fname + " " + lname
            }
            url='/about-us/?name={}'.format(fname + " " + lname)

            return HttpResponseRedirect(url)
    except:
        pass
    return render(request, "userForm.html", data)

def course(request):
    return HttpResponse("<h1>This is the Course View.</h1>")

def courseDetailsInt(request, courseid):
    return HttpResponse(f"<b>The url on the Course (int) : {courseid}.<b>")

def courseDetailsStr(request, coursestr):
    return HttpResponse(f"<b>The url on the Course (str) : {coursestr}.<b>")

def courseDetailsSlug(request, courseslug):
    return HttpResponse(f"<b>The url on the Course (slug) : {courseslug}.<b>")