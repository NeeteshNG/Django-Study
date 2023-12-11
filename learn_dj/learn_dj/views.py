from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm
import math
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contact.models import Contact

def homePage(request):
    news_data=News.objects.all()

    data = {
        'title' : 'Django Test',
        'bdata' : 'Welcome to the Django Testing.',
        'clist' : [ 'PHP', 'Java', 'Django', 'Python' ],
        'numbers' : [10,20,30,40,50,60,70],
        'student_details' : [
            { 'name' : 'Rohit', 'phone' : 9878754266},
            { 'name' : 'Deepak', 'phone' : 9878754244},
            { 'name' : 'Kapil', 'phone' : 9878754222}
        ],
        'news_data' : news_data
    }
    return render(request, "index.html", data)

def aboutUs(request):
    service_data = Service.objects.all().order_by('-service_name')
    # - is used to order the data for descending order

    paginator=Paginator(service_data, 2)
    page_number = request.GET.get('page')
    service_data_final=paginator.get_page(page_number)
    totalpage=service_data_final.paginator.num_pages

    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            service_data = Service.objects.filter(service_name__icontains=st)

    data={
        'service_data' : service_data_final,
        'last_page' : totalpage,
        'totalpagelist' : [n+1 for n in range(totalpage)]
    }

    if request.method=="GET":
        name=request.GET.get('name')
    return render(request, "about.html", data)

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        subject=request.POST.get('subject')

        contactData=Contact(first_name=fname, last_name=lname, subject=subject)

        contactData.save()

        n = "Message Sent."
    return render(request, "contact.html", {'n' : n})

def marksheet(request):
    if request.method=="POST":
        if request.POST.get('sub1') == "":
            return render(request, "marksheet.html", {'error1' : True})
        if request.POST.get('sub2') == "":
            return render(request, "marksheet.html", {'error2' : True})
        if request.POST.get('sub3') == "":
            return render(request, "marksheet.html", {'error3' : True})
        if request.POST.get('sub4') == "":
            return render(request, "marksheet.html", {'error4' : True})
        if request.POST.get('sub5') == "":
            return render(request, "marksheet.html", {'error5' : True})
        if request.POST.get('sub6') == "":
            return render(request, "marksheet.html", {'error6' : True})   
        
             
        s1=eval(request.POST.get('sub1'))
        s2=eval(request.POST.get('sub2'))
        s3=eval(request.POST.get('sub3'))
        s4=eval(request.POST.get('sub4'))
        s5=eval(request.POST.get('sub5'))
        s6=eval(request.POST.get('sub6'))


        t = s1 + s2 + s3 + s4 + s5 + s6

        p = t * 100 / 600

        if p>=60:
            d="First Division"
        elif p>=48:
            d="Second Division"
        elif p>=35:
            d="Third Division"
        else:
            d="Fail"

        data = {
            'subjects' : [s1, s2, s3, s4, s5, s6],
            'total' : t,
            'percentage' : math.floor(p),
            'division' : d
        }
        return render(request, "marksheet.html", data)
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

def newsDetails(request, slug):
    newsDetails=News.objects.get(news_slug=slug)

    data={
        'newsDetails' : newsDetails
    }
    return render(request, "newsDetails.html", data)

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